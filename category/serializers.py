from .models import CategoryModel
from rest_framework import serializers
from django.contrib.auth import get_user_model

class CategorySerializer (serializers.ModelSerializer):
    class Meta:
        model = CategoryModel
        fields = '__all__'