from rest_framework.serializers import ModelSerializer, SerializerMethodField, IntegerField
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
    like_count = IntegerField(read_only=True)
    class Meta:
        model = WorkLog
        fields = ['id', 'payload', 'is_shop', 'on_public', 'like_count', 'likelists','created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at', 'posted_feed']
