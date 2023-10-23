from .models import CustomUser
from rest_framework import serializers
from django.contrib.auth import get_user_model

class UserSerializer (serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'