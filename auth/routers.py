from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import UserRegistrationViewSet

router = DefaultRouter()
router.register('register', UserRegistrationViewSet)
