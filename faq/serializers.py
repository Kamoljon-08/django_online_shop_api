from .models import FaqModel
from rest_framework import serializers
from django.contrib.auth import get_user_model

class UserFaqSerializer (serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id', 'username')

class FaqSerializer (serializers.ModelSerializer):
    class Meta:
        model = FaqModel
        fields = '__all__'