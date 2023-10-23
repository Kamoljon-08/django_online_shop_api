from brand.models import BrandModel
from rest_framework import permissions
from category.models import CategoryModel
from .permissions import IsAuthorOrReadOnly
from django.contrib.auth import get_user_model
from rest_framework.viewsets import ModelViewSet
from .models import (
    ProductModel, 
    ProductTagModel, 
    ProductLikeModel, 
    ProductSizeModel,
    ProductColorModel, 
    ProductImageModel, 
    ProductRatingModel, 
    ProductCommentModel, 
)
from .serializers import (
    ProductSerializer,
    ProductTagSerializer,
    ProductSizeSerializer,
    ProductLikeSerializer,
    UserProductSerializer, 
    ProductColorSerializer,
    ProductImageSerializer,
    ProductRatingSerializer,
    ProductCommentSerializer,
    ProductFilterBrandSerializer,
    ProductFilterCategorySerializer,
)

# Create your views here.

"""
    admin panel for views
"""
class UserProductListViewSet (ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserProductSerializer

class UserProductDetailViewSet (ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserProductSerializer


class ProductFilterBrandViewSet (ModelViewSet):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = BrandModel.objects.all()
    serializer_class = ProductFilterBrandSerializer

class ProductFilterCategoryViewSet (ModelViewSet):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = CategoryModel.objects.all()
    serializer_class = ProductFilterCategorySerializer

class ProductFilterPriceViewSet (ModelViewSet):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = ProductModel.objects.all()
    serializer_class = ProductSerializer


class ProductListViewSet (ModelViewSet):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = ProductModel.objects.all()
    serializer_class = ProductSerializer

class ProductCreateViewSet (ModelViewSet):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = ProductModel.objects.all()
    serializer_class = ProductSerializer

class ProductUpdateViewSet (ModelViewSet):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = ProductModel.objects.all()
    serializer_class = ProductSerializer

class ProductDetailViewSet (ModelViewSet):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = ProductModel.objects.all()
    serializer_class = ProductSerializer

class ProductDeleteViewSet (ModelViewSet):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = ProductModel.objects.all()
    serializer_class = ProductSerializer


class ProductImageCreateViewSet (ModelViewSet):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = ProductImageModel.objects.all()
    serializer_class = ProductImageSerializer

class ProductImageDeleteViewSet (ModelViewSet):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = ProductImageModel.objects.all()
    serializer_class = ProductImageSerializer

class ProductImageUpdateViewSet (ModelViewSet):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = ProductImageModel.objects.all()
    serializer_class = ProductImageSerializer


class ProductCommentCreateViewSet (ModelViewSet):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = ProductCommentModel.objects.all()
    serializer_class = ProductCommentSerializer

class ProductCommentUpdateViewSet (ModelViewSet):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = ProductCommentModel.objects.all()
    serializer_class = ProductCommentSerializer

class ProductCommentDeleteViewSet (ModelViewSet):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = ProductCommentModel.objects.all()
    serializer_class = ProductCommentSerializer


class ProductLikeListViewSet (ModelViewSet):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = ProductLikeModel.objects.all()
    serializer_class = ProductLikeSerializer

class ProductLikeCreateViewSet (ModelViewSet):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = ProductLikeModel.objects.all()
    serializer_class = ProductLikeSerializer

class ProductLikeDeleteViewSet (ModelViewSet):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = ProductLikeModel.objects.all()
    serializer_class = ProductLikeSerializer


class ProductRatingCreateViewSet (ModelViewSet):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = ProductRatingModel.objects.all()
    serializer_class = ProductRatingSerializer


class ProductTagCreateViewSet (ModelViewSet):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = ProductTagModel.objects.all()
    serializer_class = ProductTagSerializer

class ProductTagUpdateViewSet (ModelViewSet):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = ProductTagModel.objects.all()
    serializer_class = ProductTagSerializer

class ProductTagDeleteViewSet (ModelViewSet):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = ProductTagModel.objects.all()
    serializer_class = ProductTagSerializer


class ProductColorCreateViewSet (ModelViewSet):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = ProductColorModel.objects.all()
    serializer_class = ProductColorSerializer

class ProductColorUpdateViewSet (ModelViewSet):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = ProductColorModel.objects.all()
    serializer_class = ProductColorSerializer

class ProductColorDeleteViewSet (ModelViewSet):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = ProductColorModel.objects.all()
    serializer_class = ProductColorSerializer


class ProductSizeCreateViewSet (ModelViewSet):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = ProductSizeModel.objects.all()
    serializer_class = ProductSizeSerializer

class ProductSizeUpdateViewSet (ModelViewSet):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = ProductSizeModel.objects.all()
    serializer_class = ProductSizeSerializer

class ProductSizeDeleteViewSet (ModelViewSet):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = ProductSizeModel.objects.all()
    serializer_class = ProductSizeSerializer