from .models import SponsorModel
from rest_framework import permissions
from .serializers import SponsorSerializer
from .permissions import IsAuthorOrReadOnly
from django.contrib.auth import get_user_model
from rest_framework.viewsets import ModelViewSet

class SponsorListView (ListView):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = SponsorModel.objects.all()
    serializer_class = SponsorSerializer

class SponsorCreateView (CreateView):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = SponsorModel.objects.all()
    serializer_class = SponsorSerializer

class SponsorDetailView (DetailView):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = SponsorModel.objects.all()
    serializer_class = SponsorSerializer

class SponsorUpdateView (UpdateView):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = SponsorModel.objects.all()
    serializer_class = SponsorSerializer

class SponsorDeleteView (DeleteView):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = SponsorModel.objects.all()
    serializer_class = SponsorSerializer