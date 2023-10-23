from .models import SponsorModel
from rest_framework import serializers
from django.contrib.auth import get_user_model

class SponsorSerializer (serializers.ModelSerializer):
    class Meta:
        model = SponsorModel
        fields = '__all__'