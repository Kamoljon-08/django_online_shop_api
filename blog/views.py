from rest_framework import permissions
from .permissions import IsAuthorOrReadOnly
from django.contrib.auth import get_user_model
from rest_framework.viewsets import ModelViewSet
from .models import BlogModel, BlogImageModel, BlogCommentModel
from .serializers import BlogSerializer, BlogImageSerializer, BlogCommentSerializer, UserBlogSerializer

class UserBlogListViewSet (ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserBlogSerializer

class UserBlogDetailViewSet (ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = BlogSerializer

class BlogListViewSet (ModelViewSet):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = BlogModel.objects.all()
    serializer_class = BlogSerializer

class BlogCreateViewSet (ModelViewSet):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = BlogModel.objects.all()
    serializer_class = BlogSerializer

class BlogDetailViewSet (ModelViewSet):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = BlogModel.objects.all()
    serializer_class = BlogSerializer

class BlogUpdateViewSet (ModelViewSet):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = BlogModel.objects.all()
    serializer_class = BlogSerializer

class BlogDeleteViewSet (ModelViewSet):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = BlogModel.objects.all()
    serializer_class = BlogSerializer

class BlogImageCreateViewSet (ModelViewSet):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = BlogImageModel.objects.all()
    serializer_class = BlogImageSerializer

class BlogImageDetailViewSet (ModelViewSet):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = BlogImageModel.objects.all()
    serializer_class = BlogImageSerializer

class BlogImageUpdateViewSet (ModelViewSet):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = BlogImageModel.objects.all()
    serializer_class = BlogImageSerializer

class BlogImageDeleteViewSet (ModelViewSet):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = BlogImageModel.objects.all()
    serializer_class = BlogImageSerializer

class BlogCommentCreateViewSet (ModelViewSet):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = BlogCommentModel.objects.all()
    serializer_class = BlogCommentSerializer

class BlogCommentUpdateViewSet (ModelViewSet):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = BlogCommentModel.objects.all()
    serializer_class = BlogCommentSerializer

class BlogCommentDeleteViewSet (ModelViewSet):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = BlogCommentModel.objects.all()
    serializer_class = BlogCommentSerializer