from rest_framework.routers import SimpleRouter
from .views import (
    UserProductListViewSet,
    UserProductDetailViewSet,

    ProductListViewSet,
    ProductCreateViewSet,
    ProductUpdateViewSet,
    ProductDetailViewSet,
    ProductDeleteViewSet,

    ProductImageCreateViewSet,
    ProductImageUpdateViewSet,
    ProductImageDeleteViewSet,

    ProductCommentCreateViewSet,
    ProductCommentDeleteViewSet,
    ProductCommentUpdateViewSet,

    ProductLikeListViewSet,
    ProductLikeCreateViewSet,
    ProductLikeDeleteViewSet,

    ProductRatingCreateViewSet,

    ProductTagCreateViewSet,
    ProductTagUpdateViewSet,
    ProductTagDeleteViewSet,

    ProductColorCreateViewSet,
    ProductColorUpdateViewSet,
    ProductColorDeleteViewSet,

    ProductSizeCreateViewSet,
    ProductSizeUpdateViewSet,
    ProductSizeDeleteViewSet,

    ProductFilterBrandViewSet,
    ProductFilterPriceViewSet,
    ProductFilterCategoryViewSet,
)

router = SimpleRouter()

router.register('user/list/', UserProductListViewSet, basename='user_product_list')
router.register('user/detail/', UserProductDetailViewSet, basename='user_product_detail')

router.register('list/', ProductListViewSet, basename='product_list')
router.register('create/', ProductCreateViewSet, basename='product_create')
router.register('detail/', ProductDetailViewSet, basename='product_detail')
router.register('update/', ProductUpdateViewSet, basename='product_update')
router.register('delete/', ProductDeleteViewSet, basename='product_delete')

router.register('image/create/', ProductImageCreateViewSet, basename='product_image_create')
router.register('image/update/', ProductImageUpdateViewSet, basename='product_image_update')
router.register('image/delete/', ProductImageDeleteViewSet, basename='product_image_delete')

router.register('comment/create/', ProductCommentCreateViewSet, basename='product_comment_create')
router.register('comment/update/', ProductCommentUpdateViewSet, basename='product_comment_update')
router.register('comment/delete/', ProductCommentDeleteViewSet, basename='product_comment_delete')

router.register('like/list/', ProductLikeListViewSet, basename='product_like_list')
router.register('like/create/', ProductLikeCreateViewSet, basename='product_like_create')
router.register('like/delete/', ProductLikeDeleteViewSet, basename='product_like_delete')

router.register('rating/create/', ProductRatingCreateViewSet, basename='product_rating_create')

router.register('tag/create/', ProductTagCreateViewSet, basename='product_tag_create')
router.register('tag/update/', ProductTagUpdateViewSet, basename='product_tag_update')
router.register('tag/delete/', ProductTagDeleteViewSet, basename='product_tag_delete')

router.register('color/create/', ProductColorCreateViewSet, basename='product_color_create')
router.register('color/update/', ProductColorUpdateViewSet, basename='product_color_update')
router.register('color/delete/', ProductColorDeleteViewSet, basename='product_color_delete')

router.register('size/create/', ProductSizeCreateViewSet, basename='product_size_create')
router.register('size/update/', ProductSizeUpdateViewSet, basename='product_size_update')
router.register('size/delete/', ProductSizeDeleteViewSet, basename='product_size_delete')

router.register('filter/brand/', ProductFilterBrandViewSet, basename='product_filter_brand')
router.register('filter/price/', ProductFilterPriceViewSet, basename='product_filter_price')
router.register('filter/category/', ProductFilterCategoryViewSet, basename='product_filter_category')

urlpatterns = router.urls