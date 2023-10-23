from rest_framework.routers import SimpleRouter
from .views import CategoryListViewSet, CategoryCreateViewSet, CategoryDetailViewSet, CategoryUpdateViewSet, CategoryDeleteViewSet

router = SimpleRouter()

router.register('list/', CategoryListViewSet, basename='category_list')
router.register('create/', CategoryCreateViewSet, basename='category_create')
router.register('detail/', CategoryDetailViewSet, basename='category_detail')
router.register('update/', CategoryUpdateViewSet, basename='category_update')
router.register('delete/', CategoryDeleteViewSet, basename='category_delete')

urlpatterns = router.urls