from rest_framework import serializers
from .models import Follow
from users.serializers import UserSerializer

class FollowSerializer(serializers.ModelSerializer):
    follower = UserSerializer(read_only=True)
    followee = UserSerializer(read_only=True)

    class Meta:
        model = Follow
        fields = ['id', 'follower', 'followee', 'created_at', 'updated_at']
