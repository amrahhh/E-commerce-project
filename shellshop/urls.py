"""shellshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from account.api.views import CustomAuthToken
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from product.views import *
from product.ckeditor_uploader import views
from django.views.decorators.cache import never_cache
from django.contrib.auth import views as auth_views

from django.conf.urls.i18n import i18n_patterns
from django.utils.translation import ugettext_lazy as _

urlpatterns = [
    path('jet/', include('jet.urls', 'jet')),  # Django JET URLS
    path('jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),  # Django JET dashboard URLS
    path('ckeditor/', include('ckeditor_uploader.urls')),
    re_path(r"^upload/", views.upload, name="ckeditor_upload"),
    re_path(r"^browse/", never_cache(views.browse), name="ckeditor_browse",),
    re_path('^', include('django.contrib.auth.urls')),
    path('social-auth/', include('social_django.urls', namespace="social")),
    path('i18n/', include('django.conf.urls.i18n')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


urlpatterns += i18n_patterns(
    path('admin/', admin.site.urls),
    path('api/', include('product.api.urls')),
    path('', include('home.urls', namespace='home')),
    path('account/', include('account.urls', namespace='account')),
    path('blog/', include('blog.urls', namespace='blog')),
    path('product/', include('product.urls', namespace='product')),
    path('contact/', include('contact.urls', namespace='contact')),
    path('checkout/', include('checkout.urls', namespace='checkout')),
    path('api/v1/checkout/', include('checkout.api.urls',)),
    path('api/auth/login/', CustomAuthToken.as_view()),
)

