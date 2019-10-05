from datetime import date

from rest_framework import views, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .models import Dish, DishInDiet, Meal
from .serializers import DishInDietSerializer, DishSerializer, MealSerializer


class AddMealView(views.APIView):

    permission_classes = [IsAuthenticated, ]

    def post(self, request):
        try:
            dish = DishInDiet.objects.get(pk=request.data.get('dish_id', None))
        except DishInDiet.DoesNotExist:
            return Response({'error': 'cannot get dish with this id'}, status=status.HTTP_400_BAD_REQUEST)
        user = self.request.user
        serializer = MealSerializer
        meal = Meal.objects.create(user=user, dish=dish)
        return Response(serializer(meal).data, status=status.HTTP_200_OK)


class TodayCaloriesView(views.APIView):

    permission_classes = [IsAuthenticated, ]

    def get(self, request):
        user = self.request.user
        dishes = DishInDiet.objects.filter(meals__user=user).filter(meals__date_created__gte=date.today())
        calories = sum([dish.get_calories() for dish in dishes])
        return Response({'calories': calories}, status=status.HTTP_200_OK)


class MostPopularDishView(views.APIView):

    def get(self, request):
        all_dishes = Dish.objects.all()
        if not all_dishes:
            return Response({'error': 'no dishes yet'}, status=status.HTTP_400_BAD_REQUEST)
        serializer = DishSerializer
        pop_dish = max(all_dishes, key=lambda d: Meal.objects.filter(dish__dish=d).count())
        return Response(serializer(pop_dish).data, status=status.HTTP_200_OK)


class ClosestDishView(views.APIView):

    def post(self, request):
        try:
            calories = int(request.data.get('calories', None))
        except SyntaxError:
            return Response({'error': 'wrong input format'}, status=status.HTTP_400_BAD_REQUEST)
        if not calories:
            return Response({'error': 'calorie content not found'}, status=status.HTTP_400_BAD_REQUEST)
        if not DishInDiet.object.all():
            return Response({'error': 'no dishes yet'}, status=status.HTTP_400_BAD_REQUEST)
        serializer = DishInDietSerializer
        closest_dish = min(DishInDiet.objects.all(), key=lambda dish: abs(dish.get_calories() - calories))
        return Response(serializer(closest_dish).data, status=status.HTTP_200_OK)
