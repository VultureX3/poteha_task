from django.urls import path

from .views import AddMealView, TodayCaloriesView, MostPopularDishView, ClosestDishView

urlpatterns = [
    path('meal/', AddMealView.as_view(), name='add_meal'),
    path('today/', TodayCaloriesView.as_view(), name='today_calories'),
    path('dish/popular/', MostPopularDishView.as_view(), name='most_popular_dish'),
    path('dish/closest/', ClosestDishView.as_view(), name='closest_dish'),
]
