from brand.models import BrandModel
from rest_framework import serializers
from category.models import CategoryModel
from django.contrib.auth import get_user_model
from .models import (
    ProductModel, 
    ProductTagModel, 
    ProductSizeModel, 
    ProductLikeModel, 
    ProductColorModel, 
    ProductImageModel, 
    ProductRatingModel, 
    ProductCommentModel
)

class ProductFilterBrandSerializer (serializers.ModelSerializer):
    class Meta:
        model = BrandModel
        fields = '__all__'

class ProductFilterCategorySerializer (serializers.ModelSerializer):
    class Meta:
        model = CategoryModel
        fields = '__all__'

class UserProductSerializer (serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id', 'username')

class ProductSerializer (serializers.ModelSerializer):
    class Meta:
        model = ProductModel
        fields = '__all__'

class ProductImageSerializer (serializers.ModelSerializer):
    class Meta:
        model = ProductImageModel
        fields = '__all__'

class ProductLikeSerializer (serializers.ModelSerializer):
    class Meta:
        model = ProductLikeModel
        fields = '__all__'

class ProductRatingSerializer (serializers.ModelSerializer):
    class Meta:
        model = ProductRatingModel
        fields = '__all__'

class ProductTagSerializer (serializers.ModelSerializer):
    class Meta:
        model = ProductTagModel
        fields = '__all__'

class ProductColorSerializer (serializers.ModelSerializer):
    class Meta:
        model = ProductColorModel
        fields = '__all__'

class ProductSizeSerializer (serializers.ModelSerializer):
    class Meta:
        model = ProductSizeModel
        fields = '__all__'

class ProductCommentSerializer (serializers.ModelSerializer):
    class Meta:
        model = ProductCommentModel
        fields = '__all__'