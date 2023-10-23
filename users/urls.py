from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import (
    UserListViewSet,
    UserCreateViewSet,
    UserDetailViewSet,
    UserUpdateViewSet,
    UserDeleteViewSet,
)

router = SimpleRouter()
router.register('list/', UserListViewSet, basename='user_list')
router.register('create/', UserCreateViewSet, basename='user_create')
router.register('detail/', UserDetailViewSet, basename='user_detail')
router.register('update/', UserUpdateViewSet, basename='user_update')
router.register('delete/', UserDeleteViewSet, basename='user_delete')

urlpatterns = router.urls