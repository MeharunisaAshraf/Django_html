from django.contrib.auth.hashers import make_password, check_password
from django.shortcuts import render, redirect, HttpResponseRedirect
from .models.product import Product
from .models.catalogue import Catalogue
from .models.customer import Customer
from .models.orders import Order
from .models.staff import Staff1
from django.http import HttpResponse
from django.views import View
from .templatetags import cart
from .middlewares.auth import simple_middleware
from django.utils.decorators import method_decorator
from django.contrib.auth.models import User
import datetime
from django.contrib.auth import authenticate, logout, login

# Create your views here.

# Cover page


class Cover(View):
    def get(self, request):
        return render(request, 'cover.html')

# creating a class for Index in which i will declare functions of different methods to call


class Index(View):

    def post(self, request):
        ViewId = request.POST.get('ViewId')
        if ViewId:
            return ViewId.image.url

        # calling product id when someone will press Add to Cart
        product = request.POST.get('product')
        decrease = request.POST.get('decrease')
        # starting session for cart
        cart = request.session.get('cart')
        print(cart)
        if cart:
            quantity = cart.get(product)
            if quantity:
                # for minus in cart
                if decrease:
                    if quantity <= 1:
                        cart.pop(product)
                    else:
                        cart[product] = quantity - 1
                else:
                    # for plus in cart and for Add to cart for first time
                    cart[product] = quantity + 1
            else:
                cart[product] = 1
        else:
            cart = {}
            cart[product] = 1

        request.session['cart'] = cart

        print('cart', request.session['cart'])
        return redirect('HomePage')

    def get(self, request):
        cart = request.session.get('cart')
        if not cart:
            request.session['cart'] = {}

        # For calling products from Product function in product.py as function of get all products is being made in product.py
        # products=Product.get_all_products();
        product = None

        # clearing cart
        # request.session.get('cart').clear()

        # For calling catalogue from Catalogue function in catalogue.py as function of get all catalogue is being made in catalogue.py
        catalogues = Catalogue.get_all_catalogue()
        # For query call on filter
        catalogueID = request.GET.get('catalogueID')
        if catalogueID:
            product = Product.get_all_products_with_catalogueid(catalogueID)
        else:
            product = Product.get_all_products()

        data = {}
        data['product'] = product
        data['catalogues'] = catalogues
        # return render(request,'orders/orders.html')
        return render(request, 'index.html', data)
        # customer as an object
        customer = Customer(Fname=Fname, Lname=Lname, PhoneNumber=PhoneNumber, Email=Email,
                            Password=Password, Address=Address, State=State, City=City, ZipCode=ZipCode)

# creating a class for signup in which i will declare functions of different methods to call


class Signup(View):
    # for signup page when method is GET, after pressign on "signup" on nav bar
    def get(self, request):
        return render(request, 'signup.html')

    # for creating account when method is POST, after pressign on button "create account"
    def post(self, request):
        Data = request.POST
        Fname = Data.get('Fname')
        Lname = Data.get('Lname')
        PhoneNumber = Data.get('PhoneNumber')
        Email = Data.get('Email')
        Password = Data.get('Password')
        Address = Data.get('Address')
        State = Data.get('State')
        City = Data.get('City')
        ZipCode = Data.get('ZipCode')
        # For passing values which have been written once by customer
        value = {'Fname': Fname, 'Lname': Lname, 'PhoneNumber': PhoneNumber, 'Email': Email,
                 'Address': Address, 'State': State, 'City': City, 'ZipCode': ZipCode}
        # customer as an object
        customer = Customer(Fname=Fname, Lname=Lname, PhoneNumber=PhoneNumber, Email=Email,
                            Password=Password, Address=Address, State=State, City=City, ZipCode=ZipCode)
        # calling the above validation function for customer here
        error_message = self.ValidationCustomer(customer)
        # Saving Values of Form
        if not error_message:
            print(Fname, Lname, PhoneNumber, Email,
                  Password, State, City, ZipCode)
        # for getting hashed password
            customer.Password = make_password(customer.Password)
        # for calling values of customer from /model/customer.py>>>>Function register
            customer.register()
        # redirecting to the home page after creating the account
            return redirect('HomePage')

        else:
            Data = {'error': error_message, 'values': value}
        return render(request, 'signup.html', Data)

    # for Validation
    def ValidationCustomer(self, customer):
        # Validation of Form Entries
        # Applying some conditions
        error_message = None
        if(not customer.Fname):
            error_message = None
        if len(customer.Fname) < 3:
            error_message = "First Name should not be less than 3 characters.."
        elif not customer.Lname:
            error_message = None
        elif len(customer.Lname) < 3:
            error_message = "Last Name should not be less than 3 characters.."
        elif not customer.PhoneNumber:
            error_message = None
        elif len(customer.PhoneNumber) < 11:
            error_message = "Phone Number must be of 11 characters.."
        elif len(customer.Password) < 8:
            error_message = "Password must be of 8 characters.."
        elif customer.EmailExistsAlready():
            error_message = "Email already exists.."

        return error_message

# creating a class of login as view in which i will define some function with different methods of call


class Login(View):

    # for middleware to return to this page after logig in
    return_url = None

    # for login page when method is GET, after pressing on "login" on nav bar
    def get(self, request):
        Login.return_url = request.GET.get('return_url')
        return render(request, 'login.html')

    # for login page when method is POST, after pressign on button "login"
    def post(self, request):
        Data = request.POST
        Email = Data.get('Email')
        Password = Data.get('Password')
        # for checking if customer email exists or not
        customer = Customer.get_customer_by_email_at_login(Email)
        error_message = None

        ##############Changings
        # for checking if staff email exists or not
        staff = Staff1.get_staff_by_email_at_login(Email)
        ##############end

        if customer:
            # for checking if password is right or not
            flag = check_password(Password, customer.Password)
            if flag:
                # creating session to save email and id of customer in session
                request.session['customer_id'] = customer.id
                request.session['customer_email'] = customer.Email

                if Login.return_url:
                    return HttpResponseRedirect(Login.return_url)
                else:
                    Login.return_url = None
                    return redirect('HomePage')

            else:
                error_message = "Wrong Password.."

        #elif request.user is not None:
            #return redirect('StaffPage')

        #######Changings
        elif staff:
            # for checking if password is right or not
            flag = check_password(Password, staff.Password)
            if flag:
                # creating session to save email in session
                request.session['staff_email'] = staff.Email
                if Login.return_url:
                    return HttpResponseRedirect(Login.return_url)
                else:
                    Login.return_url = None
                    return redirect('StaffPage')
            else:
                error_message = "Wrong Password.."
        #######end

        else:
            error_message = "Email doesn't exists.."
        return render(request, 'login.html', {'error': error_message})


class Staff(View):
    def get(self, request):
        if request.user is not None:
            order = None
            order = Order.get_all_orders()
            data = {}
            data['order'] = order
            return render(request, 'staff.html', data)
# Logout


class Logout(View):
    def get(self, request):
        request.session.clear()
        if request.user is not None:
            request.user = {}
            return redirect('CoverPage')
        return redirect('CoverPage')

# Cart


class Cart(View):
    def get(self, request):
        print()
        ids = list(request.session.get('cart').keys())
        product = Product.get_products_by_id(ids)
        print(product)
        # if not request.session.get('customer_id'):
        #         return redirect('LoginPage')
        return render(request, 'cart.html', {'product': product})

# Check Out


class CheckOut(View):
    def post(self, request):
        address = request.POST.get('Address')
        phonenumber = request.POST.get('PhoneNumber')
        customer = request.session.get('customer_id')
        cart = request.session.get('cart')
        product = Product.get_products_by_id(list(cart.keys()))
        print(address, phonenumber, customer, cart, product)

        # iterating in products which has been added in cart to get the price
        for product in product:
            print(cart.get(str(product.id)))
            order = Order(customer=Customer(id=customer),
                          product=product,
                          price=product.price,
                          address=address,
                          phonenumber=phonenumber,
                          quantity=cart.get(str(product.id)))

            if not request.session.get('customer_id'):
                return redirect('LoginPage')

            # saving the selected products as in orders
            order.placeOrder()

        # clearing cart
        request.session['cart'] = {}
        return redirect('cart')

# Orders


class OrderView(View):

    def get(self, request):
        customer = request.session.get('customer_id')
        orders = Order.get_orders_by_customer(customer)
        print(orders)
        return render(request, 'orders.html', {'orders': orders})
