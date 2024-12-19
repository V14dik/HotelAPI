from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny
from jwt_auth.serializers import UserRegistrationSerializer
from django.contrib.auth.models import User


class UserRegistrationViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer
    permission_classes = [AllowAny]
    http_method_names = ['post']  # Только метод POST, так как это регистрация
