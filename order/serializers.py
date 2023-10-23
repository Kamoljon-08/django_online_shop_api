from .models import OrderModel
from rest_framework import serializers
from django.contrib.auth import get_user_model

class UserOrderSerializer (serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id', 'username')

class OrderSerializer (serializers.ModelSerializer):
    class Meta:
        model = OrderModel
        fields = '__all__'