from .models import AdModel
from .serializers import AdSerializer
from rest_framework import permissions
from .permissions import IsAuthorOrReadOnly
from django.contrib.auth import get_user_model
from rest_framework.viewsets import ModelViewSet

# Create your views here.

class AdListViewSet (ModelViewSet):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = AdModel.objects.all()
    serializer_class = AdSerializer

class AdCreateViewSet (ModelViewSet):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = AdModel.objects.all()
    serializer_class = AdSerializer

class AdDetailViewSet (ModelViewSet):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = AdModel.objects.all()
    serializer_class = AdSerializer

class AdUpdateViewSet (ModelViewSet):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = AdModel.objects.all()
    serializer_class = AdSerializer

class AdDeleteViewSet (ModelViewSet):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = AdModel.objects.all()
    serializer_class = AdSerializer