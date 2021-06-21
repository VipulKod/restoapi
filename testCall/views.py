from django.shortcuts import render
from rest_framework import viewsets
from .models import Test
from .serializers import TestSerializer

class Test(viewsets.ModelViewSet):
    queryset = Test.objects.all()
    serializer_class = TestSerializer

