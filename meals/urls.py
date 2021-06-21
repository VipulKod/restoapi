from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'meals', views.Meals)


urlpatterns = [
   path('', include(router.urls)),
]
