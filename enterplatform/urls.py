"""enterplatform URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('baton/', include('baton.urls')),
    path('api/v1/users/', include("users.urls")),
    path('api/v1/directmessages/', include("directmessages.urls")),
    path('api/v1/donates/', include("donates.urls")),
    path('api/v1/banks/', include("banks.urls")),
    path('api/v1/feeds/', include("feeds.urls")),
    path('api/v1/genres/', include("genres.urls")),
    path('api/v1/medias/', include("medias.urls")),
    path('api/v1/notices/', include('notices.urls')),
    path('api/v1/reviews/', include("reviews.urls")),
    path('api/v1/tutorial/', include("tutorial.urls")),
    path('api/v1/votes/', include("votes.urls")),
    path('api/v1/wallets/', include("wallets.urls")),
    path('api/v1/banners/', include("banners.urls")),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
