from .models import AdModel
from rest_framework import serializers
from django.contrib.auth import get_user_model

class AdSerializer (serializers.ModelSerializer):
    class Meta:
        model = AdModel
        fields = '__all__'