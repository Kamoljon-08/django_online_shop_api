from rest_framework.routers import SimpleRouter
from .views import BasketListViewSet, BasketCreateViewSet, BasketDetailViewSet, BasketUpdateViewSet, BasketDeleteViewSet

router = SimpleRouter()

router.register('list/', BasketListViewSet, basename='basket_list')
router.register('create/', BasketCreateViewSet, basename='basket_create')
router.register('detail/', BasketDetailViewSet, basename='basket_detail')
router.register('update/', BasketUpdateViewSet, basename='basket_update')
router.register('delete/', BasketDeleteViewSet, basename='basket_delete')

urlpatterns = router.urls