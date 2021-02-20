from django import template

register = template.Library()
        
@register.filter(name = 'product_is_in_cart')
#defining a function that will tell us either the product is in cart or not
def product_is_in_cart(product , cart):
    keys = cart.keys()
    for id in keys:
        try:
            if int(id) == product.id:
                return True
        except :
            return False
        print(id,keys,product.id)           
    return False;
    

@register.filter(name = 'product_quantity_in_cart')
def product_quantity_in_cart(product , cart):
    keys = cart.keys()
    for id in keys:
        if int(id) == product.id:
            return cart.get(id) #for showing quantity of product in cart
    return 0;

#for total price of individual product in cart
@register.filter(name = 'product_total_price_in_cart')
def product_total_price_in_cart(product , cart):
    return product.price * product_quantity_in_cart(product , cart)

@register.filter(name = 'total_cart_price')
#for total price of all products in cart
def total_cart_price(product , cart):
    sum = 0;
    for product in product:
        sum += product_total_price_in_cart(product , cart)
    return sum

#filter for currency 
@register.filter(name = 'currency')
def currency(Number):
    return 'Rs ' + str(Number)

#filter to use in orders.html
@register.filter(name='multiply')
def multiply(number , number1):
    return number * number1
    