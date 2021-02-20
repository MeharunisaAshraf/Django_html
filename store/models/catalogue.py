from django.db import models

class Catalogue(models.Model):
    name = models.CharField(max_length=50)

    @staticmethod
    def get_all_catalogue():
        return Catalogue.objects.all()

    def __str__(self):
        return self.name
