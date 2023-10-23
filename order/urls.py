from rest_framework.routers import SimpleRouter
from .views import UserOrderListViewSet, OrderListViewSet, OrderCreateViewSet, OrderDetailViewSet, OrderUpdateViewSet, OrderDeleteViewSet

router = SimpleRouter()

router.register('user/list/', UserOrderListViewSet, basename='user_order_list')

router.register('list/', OrderListViewSet, basename='order_list')
router.register('create/', OrderCreateViewSet, basename='order_create')
router.register('detail/', OrderDetailViewSet, basename='order_detail')
router.register('update/', OrderUpdateViewSet, basename='order_update')
router.register('delete/', OrderDeleteViewSet, basename='order_delete')

urlpatterns = router.urls