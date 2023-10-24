from rest_framework.routers import SimpleRouter
from .views import (
    UserBlogListViewSet,
    UserBlogDetailViewSet,

    BlogListViewSet, 
    BlogCreateViewSet, 
    BlogDetailViewSet,
    BlogUpdateViewSet, 
    BlogDeleteViewSet,

    BlogImageCreateViewSet,
    BlogImageDetailViewSet,
    BlogImageUpdateViewSet,
    BlogImageDeleteViewSet,

    BlogCommentCreateViewSet,
    BlogCommentUpdateViewSet,
    BlogCommentDeleteViewSet,
)

router = SimpleRouter()
router.register('user/list/', UserBlogListViewSet, basename='user_blog_list')
router.register('user/detail/', UserBlogDetailViewSet, basename='user_blog_detail')

router.register('list/', BlogListViewSet, basename='blog_list')
router.register('create/', BlogCreateViewSet, basename='blog_create')
router.register('detail/', BlogDetailViewSet, basename='blog_detail')
router.register('update/', BlogUpdateViewSet, basename='blog_update')
router.register('delete/', BlogDeleteViewSet, basename='blog_delete')

router.register('image/create/', BlogImageCreateViewSet, basename='blog_image_create')
router.register('image/detail/', BlogImageDetailViewSet, basename='blog_image_detail')
router.register('image/update/', BlogImageUpdateViewSet, basename='blog_image_update')
router.register('image/deelte/', BlogImageDeleteViewSet, basename='blog_image_delete')

router.register('comment/create/', BlogCommentCreateViewSet, basename='blog_comment_create')
router.register('comment/update/', BlogCommentUpdateViewSet, basename='blog_comment_update')
router.register('comment/delete/', BlogCommentDeleteViewSet, basename='blog_comment_delete')

urlpatterns = router.urls