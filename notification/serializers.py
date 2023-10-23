from .models import NotificationModel
from rest_framework import serializers
from django.contrib.auth import get_user_model

class UserNotificationSerializer (serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id', 'username')

class NotificationSerializer (serializers.ModelSerializer):
    class Meta:
        model = NotificationModel
        fields = '__all__'