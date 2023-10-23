from rest_framework.routers import SimpleRouter
from .views import UserFaqListViewSet, FaqListViewSet, FaqCreateViewSet, FaqDetailViewSet, FaqUpdateViewSet, FaqDeleteViewSet

router = SimpleRouter()

router.register('user/list/', UserFaqListViewSet, basename='user_faq_list')

router.register('list/', FaqListViewSet, basename='faq_list')
router.register('create/', FaqCreateViewSet, basename='faq_create')
router.register('detail/', FaqDetailViewSet, basename='faq_detail')
router.register('update/', FaqUpdateViewSet, basename='faq_update')
router.register('delete/', FaqDeleteViewSet, basename='faq_delete')

urlpatterns = router.urls