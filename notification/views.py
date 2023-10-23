from .models import NotificationModel
from rest_framework import permissions
from .permissions import IsAuthorOrReadOnly
from django.contrib.auth import get_user_model
from rest_framework.viewsets import ModelViewSet
from .serializers import NotificationSerializer, UserNotificationSerializer

# Create your views here.

class UserNotificationListViewSet (ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserNotificationSerializer

class NotificationListViewSet (ModelViewSet):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = NotificationModel.objects.all()
    serializer_class = NotificationSerializer

class NotificationCreateViewSet (ModelViewSet):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = NotificationModel.objects.all()
    serializer_class = NotificationSerializer

class NotificationDetailViewSet (ModelViewSet):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = NotificationModel.objects.all()
    serializer_class = NotificationSerializer

class NotificationUpdateViewSet (ModelViewSet):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = NotificationModel.objects.all()
    serializer_class = NotificationSerializer

class NotificationDeleteViewSet (ModelViewSet):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = NotificationModel.objects.all()
    serializer_class = NotificationSerializer