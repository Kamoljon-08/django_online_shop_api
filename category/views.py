from .models import CategoryModel
from rest_framework import permissions
from .serializers import CategorySerializer
from .permissions import IsAuthorOrReadOnly
from django.contrib.auth import get_user_model
from rest_framework.viewsets import ModelViewSet

# Create your viewSets here.

class CategoryListViewSet (ModelViewSet):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = CategoryModel.objects.all()
    serializer_class = CategorySerializer

class CategoryCreateViewSet (ModelViewSet):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = CategoryModel.objects.all()
    serializer_class = CategorySerializer

class CategoryDetailViewSet (ModelViewSet):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = CategoryModel.objects.all()
    serializer_class = CategorySerializer

class CategoryUpdateViewSet (ModelViewSet):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = CategoryModel.objects.all()
    serializer_class = CategorySerializer

class CategoryDeleteViewSet (ModelViewSet):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = CategoryModel.objects.all()
    serializer_class = CategorySerializer