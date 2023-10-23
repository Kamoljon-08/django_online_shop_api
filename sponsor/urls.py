from rest_framework.routers import SimpleRouter
from .views import SponsorListViewSet, SponsorCreateViewSet, SponsorDetailViewSet, SponsorUpdateViewSet, SponsorDeleteViewSet

router = SimpleRouter()

router.register('list/', SponsorListViewSet, basename='sponsor_list')
router.register('create/', SponsorCreateViewSet, basename='sponsor_create')
router.register('detail/', SponsorDetailViewSet, basename='sponsor_detail')
router.register('update/', SponsorUpdateViewSet, basename='sponsor_update')
router.register('delete/', SponsorDeleteViewSet, basename='sponsor_delete')

urlpatterns = router.urls