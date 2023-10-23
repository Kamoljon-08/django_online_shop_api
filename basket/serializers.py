from .models import BasketModel
from rest_framework import serializers
from django.contrib.auth import get_user_model

class BasketSerializer (serializers.ModelSerializer):
    class Meta:
        model = BasketModel
        fields = '__all__'