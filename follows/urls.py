from django.urls import path
from .views import FollowToggleView, FollowListView

urlpatterns = [
    path('', FollowToggleView.as_view(), name='follow-toggle'),
    path('list/', FollowListView.as_view(), name='follow-list'),
]
