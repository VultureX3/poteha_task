from django.urls import path

from .views import AddMealView

urlpatterns = [
    path('add_meal/', AddMealView.as_view(), name='add_meal'),
]
