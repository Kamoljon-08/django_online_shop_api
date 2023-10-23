from rest_framework.routers import SimpleRouter
from .views import UserNotificationListViewSet, NotificationListViewSet, NotificationCreateViewSet, NotificationDetailViewSet, NotificationUpdateViewSet, NotificationDeleteViewSet

router = SimpleRouter()

router.register('contact/', UserNotificationListViewSet, basename='user_contact')

router.register('list/', NotificationListViewSet, basename='notification_list')
router.register('create/', NotificationCreateViewSet, basename='notification_create')
router.register('detail/', NotificationDetailViewSet, basename='notification_detail')
router.register('update/', NotificationUpdateViewSet, basename='notification_update')
router.register('delete/', NotificationDeleteViewSet, basename='notification_delete')

urlpatterns = router.urls