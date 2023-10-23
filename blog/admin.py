from django.contrib import admin
from .models import BlogModel, BlogImageModel, BlogCommentModel

# Register your models here.


admin.site.register(BlogModel)
admin.site.register(BlogImageModel)
admin.site.register(BlogCommentModel)