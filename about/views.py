from rest_framework import permissions
from .permissions import IsAuthorOrReadOnly
from django.contrib.auth import get_user_model
from rest_framework.viewsets import ModelViewSet
from .models import CompanyFileModel, CompanyMemberModel
from .serializers import CompanyFileSerializer, UserAboutSerializer, AboutMemberSerializer

# Create your views here.

class UserAboutListViewSet (ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserAboutSerializer

class CompanyFileListViewSet (ModelViewSet):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = CompanyFileModel.objects.all()
    serializer_class = CompanyFileSerializer

class CompanyFileCreateViewSet (ModelViewSet):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = CompanyFileModel.objects.all()
    serializer_class = CompanyFileSerializer

class CompanyFileDetailViewSet (ModelViewSet):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = CompanyFileModel.objects.all()
    serializer_class = CompanyFileSerializer

class CompanyFileUpdateViewSet (ModelViewSet):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = CompanyFileModel.objects.all()
    serializer_class = CompanyFileSerializer

class CompanyFileDeleteViewSet (ModelViewSet):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = CompanyFileModel.objects.all()
    serializer_class = CompanyFileSerializer

class CompanyMemberCreateViewSet (ModelViewSet):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = CompanyFileModel.objects.all()
    serializer_class = CompanyFileSerializer

class CompanyMemberUpdateViewSet (ModelViewSet):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = CompanyFileModel.objects.all()
    serializer_class = CompanyFileSerializer

class CompanyMemberDetailViewSet (ModelViewSet):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = CompanyFileModel.objects.all()
    serializer_class = CompanyFileSerializer

class CompanyMemberDeleteViewSet (ModelViewSet):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = CompanyFileModel.objects.all()
    serializer_class = CompanyFileSerializer