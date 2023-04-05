from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('user-info/', views.UserInfoView.as_view(), name='user_info'),
    path('register/', views.Register.as_view(), name='register'),
    # Add other URL patterns as needed
]