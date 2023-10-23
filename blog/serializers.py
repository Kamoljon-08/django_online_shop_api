from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import BlogModel, BlogImageModel, BlogCommentModel

class UserBlogSerializer (serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id', 'username')

class BlogSerializer (serializers.ModelSerializer):
    class Meta:
        model = BlogModel
        fields = '__all__'

class BlogImageSerializer (serializers.ModelSerializer):
    class Meta:
        model = BlogImageModel
        fields = '__all__'

class BlogCommentSerializer (serializers.ModelSerializer):
    class Meta:
        model = BlogCommentModel
        fields = '__all__'