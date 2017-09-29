from django.db import models

# Create your models here.
class Category(models.Model):
    category = models.CharField(max_length=200)

    def __str__(self):
        return self.category


class Subcategory(models.Model):
    category = models.ForeignKey(Category)
    subcategory = models.CharField(max_length=200)

    def __str__(self):
        return self.subcategory

class Product(models.Model):
    product_category = models.ForeignKey(Category)
    product_subcategory = models.ForeignKey(Subcategory, blank = True)

    product_name = models.CharField(max_length=200)
    product_price = models.FloatField(default=0)


    def __str__(self):
        return self.product_name