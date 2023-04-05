from django.urls import path
from . import views

urlpatterns = [
    path("", views.FeedList.as_view(), name="feed-list"),
    path("<int:pk>/", views.FeedDetail.as_view(), name="feed-detail"),
    path("<int:feed_pk>/worklogs/", views.WorkLogList.as_view(), name="worklog-list"),
    path("<int:feed_pk>/worklogs/<int:pk>/", views.WorkLogDetail.as_view(), name="worklog-detail"),
]



