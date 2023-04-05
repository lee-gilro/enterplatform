from django.db.models import Subquery, OuterRef
from rest_framework import permissions
from rest_framework import generics
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import Feed, WorkLog
from .serializers import FeedSerializer, WorkLogSerializer
from .permissions import IsOwnerOrReadOnly
from users.models import User
from follows.models import Follow
# Create your views here.

class FeedList(generics.ListCreateAPIView): #feed list 을 보여주는 view
    queryset = Feed.objects.all()
    serializer_class = FeedSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    http_method_names = ['get']

class FeedDetail(generics.RetrieveUpdateDestroyAPIView): #feed detail 을 보여주는 view, 수정가능
    queryset = Feed.objects.all()
    serializer_class = FeedSerializer
    authentication_classes = [JWTAuthentication, SessionAuthentication, BasicAuthentication]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    http_method_names = ['get', 'put']

class WorkLogList(generics.ListCreateAPIView): #worklog list 을 보여주는 view, 워크로그 생산가능
    queryset = WorkLog.objects.all()
    serializer_class = WorkLogSerializer
    authentication_classes = [JWTAuthentication, SessionAuthentication, BasicAuthentication]  
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    http_method_names = ['get', 'post']

    def get_queryset(self):
        queryset = super().get_queryset()
        feed_pk = self.kwargs['feed_pk']
        if feed_pk is not None:
            queryset = queryset.filter(posted_feed_id=feed_pk)
        return queryset
    
    def perform_create(self, serializer):
        # Get the user's feed
        user_feed = self.request.user.feeds # type: ignore
        print(user_feed)
        serializer.save(posted_feed=user_feed)

class WorkLogDetail(generics.RetrieveUpdateDestroyAPIView): #worklog detail 을 보여주는 view, 수정가능 인스타그램의 홈화면처럼 보여짐,
    serializer_class = WorkLogSerializer
    authentication_classes = [JWTAuthentication, SessionAuthentication, BasicAuthentication]  
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    http_method_names = ['get', 'put', 'delete']

    def get_queryset(self):
        queryset = WorkLog.objects.all()
        feed_pk = self.kwargs['feed_pk']
        if feed_pk is not None:
            queryset = queryset.filter(posted_feed_id=feed_pk)
        return queryset



class FollowedUsersWorkLogList(generics.ListAPIView):
    serializer_class = WorkLogSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_recommended_users(self):
        return User.objects.order_by('-date_joined')[:5]  # Fetch the 5 most recent users, adjust as needed

    def get_queryset(self):
        user = self.request.user
        followed_users = Follow.objects.filter(follower=user).values_list('followee', flat=True)

        if not followed_users:
            followed_users = [u.id for u in self.get_recommended_users()]
        # Get the latest worklog for each user
        latest_worklogs = WorkLog.objects.filter(
            posted_feed__user_id=OuterRef('pk')
        ).order_by('-created_at')

        # Annotate the users queryset with the latest worklog's id
        followed_users_with_latest_worklog = User.objects.filter(
            id__in=followed_users
        ).annotate(latest_worklog_id=Subquery(latest_worklogs.values('id')[:1]))

        # Get the worklogs corresponding to the latest worklog ids
        queryset = WorkLog.objects.filter(
            id__in=followed_users_with_latest_worklog.values('latest_worklog_id')
        ).order_by('-created_at')

        return queryset


