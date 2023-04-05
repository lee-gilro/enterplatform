from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from feeds.models import WorkLog
from reviews.models import Review
from reviews.serializers import ReviewSerializer
from rest_framework import permissions

class ReviewPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        if request.user.is_authenticated and (request.user == obj.user or request.user == obj.worklog.user):
            return True
        return False

class ReviewAPIView(GenericAPIView):

    serializer_class = ReviewSerializer
    permission_classes = [ReviewPermission]

    def get_queryset(self):
        worklog_id = self.kwargs['worklog_id']
        return Review.objects.filter(worklog_id=worklog_id)

    def get(self, request, worklog_id):
        reviews = self.get_queryset()
        serializer = self.get_serializer(reviews, many=True)
        return Response(serializer.data)

    def post(self, request, worklog_id):
        worklog = get_object_or_404(WorkLog, id=worklog_id)
        replay = request.data.get('replay')
        user = request.user

        review = Review(user=user, worklog=worklog, replay=replay)
        review.save()

        serializer = self.get_serializer(review)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def delete(self, request, worklog_id, review_id):
        review = get_object_or_404(Review, id=review_id)
        self.check_object_permissions(request, review)
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
