from django.conf import settings
from django.utils import timezone
from django.db import transaction
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.status import HTTP_204_NO_CONTENT
from rest_framework.response import Response
from rest_framework.exceptions import NotFound, NotAuthenticated, ParseError, PermissionDenied
from .models import Feed, WorkLog
from . import serializers

SAFE_METHODS = ('GET',)

class Feeds(APIView):
    
    def get(self, request):
        all_feeds = Feed.objects.all()
        serializer = serializers.FeedSerializer(all_feeds, many = True,)
        return Response(serializer.data)
    
class FeedDetails(APIView):
    def get_object(self, pk):
        try:
            return Feed.objects.get(pk=pk)
        except Feed.DoesNotExist:
            return NotFound
        
    def get(self, request, pk):
        feed = self.get_object(pk=pk)
        return Response(serializers.FeedSerializer(feed).data)