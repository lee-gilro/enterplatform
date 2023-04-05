from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Follow
from .serializers import FollowSerializer


class FollowToggleView(generics.GenericAPIView):
    queryset = Follow.objects.all()
    serializer_class = FollowSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        follower = self.request.user
        followee_id = request.data.get("followee")
        
        if not followee_id:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        follow, created = Follow.objects.get_or_create(follower=follower, followee_id=followee_id)

        if created:
            return Response(self.get_serializer(follow).data, status=status.HTTP_201_CREATED)
        else:
            follow.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)



class FollowListView(generics.ListAPIView):
    serializer_class = FollowSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Follow.objects.filter(follower=user)
