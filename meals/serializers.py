#Serializers converts data to and from JSON

from rest_framework import serializers
from .models import Meal

class MealsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meal
        fields = ('id', 'name', 'ingredients', 'price', 'vegetarian', 'typeOfFood', 'photo', 'list_date')