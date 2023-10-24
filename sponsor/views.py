from .models import SponsorModel
from rest_framework import permissions
from .serializers import SponsorSerializer
from .permissions import IsAuthorOrReadOnly
from django.contrib.auth import get_user_model
from rest_framework.viewsets import ModelViewSet

class SponsorListViewSet (ModelViewSet):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = SponsorModel.objects.all()
    serializer_class = SponsorSerializer

class SponsorCreateViewSet (ModelViewSet):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = SponsorModel.objects.all()
    serializer_class = SponsorSerializer

class SponsorDetailViewSet (ModelViewSet):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = SponsorModel.objects.all()
    serializer_class = SponsorSerializer

class SponsorUpdateViewSet (ModelViewSet):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = SponsorModel.objects.all()
    serializer_class = SponsorSerializer

class SponsorDeleteViewSet (ModelViewSet):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = SponsorModel.objects.all()
    serializer_class = SponsorSerializer