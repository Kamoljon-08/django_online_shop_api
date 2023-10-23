from .models import BasketModel
from rest_framework import permissions
from .serializers import BasketSerializer
from .permissions import IsAuthorOrReadOnly
from django.contrib.auth import get_user_model
from rest_framework.viewsets import ModelViewSet

class BasketListViewSet (ModelViewSet):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = BasketModel.objects.all()
    serializer_class = BasketSerializer

class BasketCreateViewSet (ModelViewSet):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = BasketModel.objects.all()
    serializer_class = BasketSerializer

class BasketDetailViewSet (ModelViewSet):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = BasketModel.objects.all()
    serializer_class = BasketSerializer

class BasketUpdateViewSet (ModelViewSet):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = BasketModel.objects.all()
    serializer_class = BasketSerializer

class BasketDeleteViewSet (ModelViewSet):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = BasketModel.objects.all()
    serializer_class = BasketSerializer