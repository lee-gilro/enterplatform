from rest_framework.serializers import ModelSerializer

from rest_framework import serializers

class LikeCountSerializer(ModelSerializer):
    like_count = serializers.IntegerField()
