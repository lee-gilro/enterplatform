from django.urls import path
from . import views


urlpatterns = [
    path("auth", views.Auth.as_view()),
    path("register/", views.Register.as_view()), # post - 회원가입

]
# @/users/@username/reviews