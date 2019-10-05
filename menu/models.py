from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):

    name = models.CharField(max_length=60)
    calories = models.DecimalField(max_digits=7, decimal_places=2)


class Dish(models.Model):

    name = models.CharField(max_length=60)
    description = models.TextField(max_length=1000, blank=True)
    photo = models.URLField(max_length=1000, blank=True)  # link


class DishInDiet(models.Model):

    dish = models.ForeignKey(Dish, on_delete=models.CASCADE, related_name='in_diet')
    products = models.ManyToManyField(Product, related_name='products')

    def calories(self):
        return sum(self.products.calories)


class Meal(models.Model):

    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='meals')
    dish = models.ForeignKey(DishInDiet, on_delete=models.DO_NOTHING, related_name='meals')
