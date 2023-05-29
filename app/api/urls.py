from django.urls import path, include
from .views import CommandViewSet, IceCreamViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'command', CommandViewSet, basename="command")
router.register(r'icecream', IceCreamViewSet, basename="icecream")

urlpatterns = [
    path('', include(router.urls)),
]