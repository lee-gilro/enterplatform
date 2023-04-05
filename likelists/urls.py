from django.urls import path
from .views import LikeListToggle

urlpatterns = [
    path('worklog/<int:worklog_pk>/toggle-like/', LikeListToggle.as_view(), name='toggle-like'),
]