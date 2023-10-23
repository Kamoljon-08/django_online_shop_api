"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title='Users Api',
        description='Oddiy user project APIsi',
        default_version='v1',
        terms_of_service='http://www.google.com/policcies/terms/',
        contact=openapi.Contact(email='axmatovkamoljon08@gmail.com'),
        license=openapi.License(name='Users project litsenziyasi'),       
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include('users.urls')),
    path('about/', include('about.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('api/v1/dj-rest-auth/', include('dj_rest_auth.urls')),
    path('api/v1/dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')),
    path('api/allauth/', include('allauth.urls')),
    path('swagger/', schema_view.with_ui(
        'swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui(
        'redoc', cache_timeout=0), name='schema-redoc'),
]

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('admin_panel/', PageView.as_view(), name='admin_panel'),

#     path('ad/', include('ad.urls')),
#     path('faq/', include('faq.urls')),
#     path('blog/', include('blog.urls')),
#     path('user/', include('users.urls')),
#     path('about/', include('about.urls')),
#     path('brand/', include('brand.urls')),
#     path('sponsor/', include('sponsor.urls')),
#     path('product/', include('product.urls')),
#     path('category/', include('category.urls')),
#     path('basket/', include('basket.urls')),
#     path('notification/', include('notification.urls')),
#     path('order/', include('order.urls')),
# ] 