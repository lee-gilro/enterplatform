from rest_framework import serializers
from .models import Banner

class PublicBannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banner
        fields = (
            "pk",
            "title",
            "context",
            "created_at",
        )