from django.shortcuts import render
from rest_framework import generics, views, viewsets, status
from rest_framework.response import Response

from .models import User, DishInDiet, Meal


class AddMealView(views.APIView):

    def post(self, request, *args, **kwargs):
        try:
            dish = DishInDiet.objects.get(pk=request.data.get('dish_id', None))
        except DishInDiet.DoesNotExist:
            return Response({'status': 'cannot get dish with this id'}, status=status.HTTP_400_BAD_REQUEST)
        user = self.request.user
        meal = Meal.objects.create(user=user, dish=dish)
        return Response(meal, status=status.HTTP_200_OK)


