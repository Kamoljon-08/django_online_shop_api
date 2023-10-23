from .models import CustomUser
from rest_framework import permissions
from .permissions import IsAuthorOrReadOnly
from django.contrib.auth import get_user_model
from rest_framework.viewsets import ModelViewSet
from .serializers import UserSerializer

# Create your views here.
        
class UserListViewSet (ModelViewSet):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

class UserCreateViewSet (ModelViewSet):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

class UserDetailViewSet (ModelViewSet):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

class UserUpdateViewSet (ModelViewSet):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

class UserDeleteViewSet (ModelViewSet):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
