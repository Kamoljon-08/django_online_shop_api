from .models import BrandModel
from rest_framework import permissions
from .serializers import BrandSerializer
from .permissions import IsAuthorOrReadOnly
from django.contrib.auth import get_user_model
from rest_framework.viewsets import ModelViewSet

# Create your views here.

class BrandListViewSet (ModelViewSet):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = BrandModel.objects.all()
    serializer_class = BrandSerializer

class BrandCreateViewSet (ModelViewSet):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = BrandModel.objects.all()
    serializer_class = BrandSerializer

class BrandDetailViewSet (ModelViewSet):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = BrandModel.objects.all()
    serializer_class = BrandSerializer

class BrandUpdateViewSet (ModelViewSet):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = BrandModel.objects.all()
    serializer_class = BrandSerializer

class BrandDeleteViewSet (ModelViewSet):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = BrandModel.objects.all()
    serializer_class = BrandSerializer