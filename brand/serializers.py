from .models import BrandModel
from rest_framework import serializers
from django.contrib.auth import get_user_model

class BrandSerializer (serializers.ModelSerializer):
    class Meta:
        model = BrandModel
        fields = '__all__'