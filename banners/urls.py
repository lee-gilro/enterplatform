from django.urls import path
from . import views


urlpatterns = [
    path("", views.Banners.as_view()),
]