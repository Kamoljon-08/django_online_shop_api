from .models import OrderModel
from rest_framework import permissions
from .permissions import IsAuthorOrReadOnly
from django.contrib.auth import get_user_model
from rest_framework.viewsets import ModelViewSet
from .serializers import OrderSerializer, UserOrderSerializer

class UserOrderListViewSet (ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserOrderSerializer

class OrderListViewSet (ModelViewSet):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = OrderModel.objects.all()
    serializer_class = OrderSerializer

class OrderCreateViewSet (ModelViewSet):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = OrderModel.objects.all()
    serializer_class = OrderSerializer

class OrderDetailViewSet (ModelViewSet):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = OrderModel.objects.all()
    serializer_class = OrderSerializer

class OrderUpdateViewSet (ModelViewSet):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = OrderModel.objects.all()
    serializer_class = OrderSerializer

class OrderDeleteViewSet (ModelViewSet):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = OrderModel.objects.all()
    serializer_class = OrderSerializer