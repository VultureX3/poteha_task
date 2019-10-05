from rest_framework import serializers

from .models import Dish, DishInDiet, Meal


class DishSerializer(serializers.ModelSerializer):

    class Meta:
        model = Dish
        fields = '__all__'


class DishInDietSerializer(serializers.ModelSerializer):

    class Meta:
        model = DishInDiet
        fields = '__all__'


class MealSerializer(serializers.ModelSerializer):

    class Meta:
        model = Meal
        fields = '__all__'
        read_only_fields = ('date_created',)
