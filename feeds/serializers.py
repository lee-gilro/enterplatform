from rest_framework.serializers import ModelSerializer, SerializerMethodField
from .models import Feed, WorkLog
from users.serializers import TinyUserSerializer, PrivateUserSerializer

class FeedSerializer(ModelSerializer):
    class Meta:
        model = Feed
        fields = (
            "pk",
            "user",
            "worklogs",
        )

class WorkLogSerializer(ModelSerializer):
    class Meta:
        model = WorkLog
        fields = (
            "posted_feed",
            "payload",
            "is_shop",
            "photos",
        )