from rest_framework.routers import SimpleRouter
from .views import (
    UserAboutListViewSet,
    
    CompanyFileListViewSet,
    CompanyFileCreateViewSet,
    CompanyFileDetailViewSet,
    CompanyFileUpdateViewSet,
    CompanyFileDeleteViewSet,

    CompanyMemberCreateViewSet,
    CompanyMemberDetailViewSet,
    CompanyMemberUpdateViewSet,
    CompanyMemberDeleteViewSet,
)

router = SimpleRouter()

router.register('user/list/', UserAboutListViewSet, basename='user_about_list')

router.register('file/list/', CompanyFileListViewSet, basename='about_file_list')
router.register('file/create/', CompanyFileCreateViewSet, basename='about_file_create')
router.register('file/detail/', CompanyFileDetailViewSet, basename='about_file_detail')
router.register('file/update/', CompanyFileUpdateViewSet, basename='about_file_update')
router.register('file/delete/', CompanyFileDeleteViewSet, basename='about_file_delete')

router.register('member/create/', CompanyMemberCreateViewSet, basename='about_member_create')
router.register('member/detail/', CompanyMemberDetailViewSet, basename='about_member_detail')
router.register('member/update/', CompanyMemberUpdateViewSet, basename='about_member_update')
router.register('member/delete/', CompanyMemberDeleteViewSet, basename='about_member_delete')

urlpatterns = router.urls