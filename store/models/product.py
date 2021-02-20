from django.db import models
# foreign key reference
from .catalogue import Catalogue

class Product (models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField(default=0)
    description = models.CharField(max_length=500,default='')
    image = models.ImageField(upload_to='product/')
# foreign key call
    catalogue = models.ForeignKey(
        Catalogue, on_delete=models.CASCADE, default=1)

    @staticmethod
    def get_all_products():
        return Product.objects.all()

    @staticmethod
    def get_all_products_with_catalogueid(catalogue_id):
        if catalogue_id:
            return Product.objects.filter(catalogue=catalogue_id)
        else:
            return Product.get_all_products()
#for cart
    @staticmethod
    def get_products_by_id(ids):
        return Product.objects.filter(id__in = ids )
