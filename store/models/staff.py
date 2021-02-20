from django.db import models

class Staff1 (models.Model):
    Fname = models.CharField(max_length=50)
    Lname = models.CharField(max_length=50)
    PhoneNumber = models.IntegerField()
    Email = models.EmailField()
    Password = models.CharField(max_length=100)
# for saving values of staff as an object

    def register(self):
        self.save()

# for passing email to login
    @staticmethod
    def get_staff_by_email_at_login(Email):
        try:
            return Staff1.objects.get(Email = Email)
        except:
            return False