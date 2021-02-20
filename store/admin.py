from django.contrib import admin
#Register your models here.

#For list view
class AdminProduct(admin.ModelAdmin):
    list_display = ['name','price','catalogue']
#Product Table registered here as
from .models.product import Product
admin.site.register(Product,AdminProduct)

#For list view
class AdminCatalogue(admin.ModelAdmin):
    list_display = ['name']
#Catalogue Table registered here as
from .models.catalogue import Catalogue
admin.site.register(Catalogue,AdminCatalogue)

#For list view
class AdminCustomer(admin.ModelAdmin):
    list_display = ['Fname','Lname','PhoneNumber','Email','Password','Address','State','City','ZipCode']
#Customer Table(Model) registered here as
from .models.customer import Customer
admin.site.register(Customer,AdminCustomer)

#For list view
class AdminOrder(admin.ModelAdmin):
    list_display = ['product','customer','quantity','price','address','phonenumber','date','status']
#Order Table(Model) registered here as
from .models.orders import Order
admin.site.register(Order,AdminOrder)

#For list view
class AdminStaff(admin.ModelAdmin):
    list_display = ['Fname','Lname','PhoneNumber','Email','Password']
#Staff Table(Model) registered here as
from .models.staff import Staff1
admin.site.register(Staff1,AdminStaff)