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
    
    def put(self, request, pk):
        feed = self.get_object(pk=pk)
        serializer = serializers.FeedSerializer(feed, data=request.data, partial=True)
        if serializer.is_valid():
            feed = serializer.save()
            serializer = serializers.FeedSerializer(feed)
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        
    def post(self, request, pk):
        feed = self.get_object(pk=pk)
        serializer = serializers.WorkLogSerializer(data=request.data)
        if serializer.is_valid():
            worklog = serializer.save(posted_feed=feed)
            serializer = serializers.WorkLogSerializer(worklog)
            return Response(serializer.data)
        else:
            return Response(serializer.errors)