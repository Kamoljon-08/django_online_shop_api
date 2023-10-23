from django.contrib import admin
from .models import (
    ProductModel, 
    ProductImageModel, 
    ProductColorModel, 
    ProductTagModel, 
    ProductCommentModel, 
    ProductSizeModel, 
    ProductLikeModel, 
    ProductRatingModel,
)

# Register your models here.

admin.site.register(ProductModel)
admin.site.register(ProductLikeModel)
admin.site.register(ProductRatingModel)
admin.site.register(ProductColorModel)
admin.site.register(ProductCommentModel)
admin.site.register(ProductImageModel)
admin.site.register(ProductSizeModel)
admin.site.register(ProductTagModel)
