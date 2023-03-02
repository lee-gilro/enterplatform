from rest_framework.serializers import ModelSerializer
from feeds.serializers import WorkLogSerializer
from .models import LikeList

class LikeListSerializer(ModelSerializer):

    rooms = WorkLogSerializer(many=True, read_only =True)

    class Meta:
            model = LikeList
            fields = (
                "pk",
                "name",
                "worklog",
            )
