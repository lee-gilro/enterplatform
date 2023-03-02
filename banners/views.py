from django.conf import settings
from django.utils import timezone
from django.db import transaction
from rest_framework.views import APIView
from rest_framework.status import HTTP_204_NO_CONTENT
from rest_framework.response import Response
from rest_framework.exceptions import NotFound, NotAuthenticated, ParseError, PermissionDenied
from .models import Banner
from . import serializers

SAFE_METHODS = ('GET',)

class Banners(APIView):
    
    def get(self, request):
        all_banners = Banner.objects.filter(on_public = True, )
        serializer = serializers.PublicBannerSerializer(all_banners, many= True,)
        return Response(serializer.data)