from django.shortcuts import render
from rest_framework import viewsets
from .models import Meal
from .serializers import MealsSerializer

class Meals(viewsets.ModelViewSet):
    queryset = Meal.objects.all()
    serializer_class = MealsSerializer

