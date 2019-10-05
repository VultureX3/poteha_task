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

    name = models.CharField(max_length=60)
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE, related_name='in_diet')

    def get_calories(self):
        ingredients = Ingredients.objects.filter(dish=self)
        calories = sum(i.amount * i.product.calories / 100 for i in ingredients)
        return calories


class Meal(models.Model):

    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='meals')
    dish = models.ForeignKey(DishInDiet, on_delete=models.DO_NOTHING, related_name='meals')
    date_created = models.DateTimeField(auto_now_add=True)


class Ingredients(models.Model):

    dish = models.ForeignKey(DishInDiet, on_delete=models.CASCADE, related_name='ingredients')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='products')
    amount = models.IntegerField()
