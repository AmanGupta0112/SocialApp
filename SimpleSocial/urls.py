"""SimpleSocial URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path
from django.conf.urls import url,include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    path('admin/', admin.site.urls),
    url(r'^$',views.HomeView.as_view(),name='home'),
    url(r'^test/$',views.TestView.as_view(),name='test'),
    url(r'^thanks/$',views.ThankView.as_view(),name='thanks'),
    url(r'^accounts/', include('accounts.urls', namespace='accounts')),
    url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^posts/',include('posts.urls',namespace='posts')),
    # url(r'^profile_user/',include('profile_user.urls',namespace= 'profile_user')),
    url(r'^groups/',include('groups.urls',namespace='groups')),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

# if settings.DG:
#     urlpatterns +=
