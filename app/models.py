from django.db import models


class Flavors(models.Model):
    flavor = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    available = models.BooleanField(default=True)
    seasonal = models.BooleanField(default=False)
    image = models.CharField(max_length=500)

    def __str__(self):
        return self.flavor


class Inventory(models.Model):
    ingredient_name = models.CharField(max_length=50)
    quantity = models.PositiveIntegerField()
    unit = models.CharField(max_length=50)

    def __str__(self):
        return self.ingredient_name


class Customer_Suggestions(models.Model):
    customer_name = models.CharField(max_length=50)
    customer_email = models.EmailField()
    flavor_suggestion = models.CharField(max_length=50)
    allergy_concern = models.CharField(max_length=200)
