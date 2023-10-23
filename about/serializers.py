from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import CompanyFileModel, CompanyMemberModel

class CompanyFileSerializer (serializers.ModelSerializer):
    class Meta:
        model = CompanyFileModel
        fields = '__all__'

class UserAboutSerializer (serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id', 'username')

class AboutMemberSerializer (serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id', 'username')