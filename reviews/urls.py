from django.urls import path
from . import views
from reviews.views import ReviewAPIView

urlpatterns = [
    path('worklogs/<int:worklog_id>/reviews/', ReviewAPIView.as_view(), name='reviews'),
    path('worklogs/<int:worklog_id>/reviews/<int:review_id>/', ReviewAPIView.as_view(), name='review_detail'),
]
