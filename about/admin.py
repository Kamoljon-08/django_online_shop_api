from django.contrib import admin
from .models import CompanyFileModel, CompanyMemberModel

# Register your models here.

admin.site.register(CompanyFileModel)
admin.site.register(CompanyMemberModel)