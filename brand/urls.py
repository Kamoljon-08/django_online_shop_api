from rest_framework.routers import SimpleRouter
from .views import BrandListViewSet, BrandCreateViewSet, BrandDetailViewSet, BrandUpdateViewSet, BrandDeleteViewSet

router = SimpleRouter()

router.register('list/', BrandListViewSet, basename='brand_list')
router.register('create/', BrandCreateViewSet, basename='brand_create')
router.register('detail/', BrandDetailViewSet, basename='brand_detail')
router.register('update/', BrandUpdateViewSet, basename='brand_update')
router.register('delete/', BrandDeleteViewSet, basename='brand_delete')

urlpatterns = router.urls