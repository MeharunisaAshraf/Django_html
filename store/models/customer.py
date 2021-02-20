from django.db import models

class Customer (models.Model):
    Fname = models.CharField(max_length=50)
    Lname = models.CharField(max_length=50)
    PhoneNumber = models.IntegerField()
    Email = models.EmailField()
    Password = models.CharField(max_length=100)
    Address = models.CharField(max_length=100)
    State = models.CharField(max_length=50)
    City = models.CharField(max_length=50)
    ZipCode = models.IntegerField()
# for saving values of customer as an object

    def register(self):
        self.save()
# for checking if customer with same email exits already

    def EmailExistsAlready(self):
        if Customer.objects.filter(Email = self.Email):
            return True

        return False
# for passing email to login 
    @staticmethod
    def get_customer_by_email_at_login(Email):
        try:
            return Customer.objects.get(Email = Email)
        except:
            return False