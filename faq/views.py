from .models import FaqModel
from rest_framework import permissions
from .permissions import IsAuthorOrReadOnly
from django.contrib.auth import get_user_model
from rest_framework.viewsets import ModelViewSet
from .serializers import FaqSerializer, UserFaqSerializer

# Create your viewSets here.

class UserFaqListViewSet (ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserFaqSerializer

class FaqListViewSet (ModelViewSet):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = FaqModel.objects.all()
    serializer_class = FaqSerializer

class FaqCreateViewSet (ModelViewSet):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = FaqModel.objects.all()
    serializer_class = FaqSerializer

class FaqUpdateViewSet (ModelViewSet):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = FaqModel.objects.all()
    serializer_class = FaqSerializer

class FaqDetailViewSet (ModelViewSet):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = FaqModel.objects.all()
    serializer_class = FaqSerializer

class FaqDeleteViewSet (ModelViewSet):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = FaqModel.objects.all()
    serializer_class = FaqSerializer