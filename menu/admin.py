from django.contrib import admin

from .models import Product, Dish, DishInDiet, Meal, Ingredients

admin.site.register(Product)
admin.site.register(Dish)
admin.site.register(DishInDiet)
admin.site.register(Meal)
admin.site.register(Ingredients)
