from rest_framework.routers import SimpleRouter
from .views import (
    AdListViewSet,
    AdCreateViewSet,
    AdDetailViewSet,
    AdUpdateViewSet,
    AdDeleteViewSet,
)

router = SimpleRouter()

router.register('list/', AdListView, basename='ad_list')
router.register('create/', AdCreateViewSet, basename='ad_create')
router.register('detail/', AdDetailViewSet, basename='ad_detail')
router.register('update/', AdUpdateViewSet, basename='ad_update')
router.register('deelte/', AdDeleteViewSet, basename='ad_delete')

urlpatterns = router.urls