from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import NotFound
from rest_framework.status import HTTP_200_OK
from .models import LikeList
from .serializers import LikeCountSerializer
from feeds.models import WorkLog


class LikeListToggle(APIView):
    permission_classes = [IsAuthenticated]

    def get_list(self, user):
        try:
            return LikeList.objects.get(user=user)
        except LikeList.DoesNotExist:
            raise NotFound

    def get_worklog(self, pk):
        try:
            return WorkLog.objects.get(pk=pk)
        except WorkLog.DoesNotExist:
            raise NotFound

    def put(self, request, worklog_pk):
        likelist = self.get_list(request.user)
        worklog = self.get_worklog(worklog_pk)

        if likelist.worklogs.filter(pk=worklog.pk).exists():
            likelist.worklogs.remove(worklog)
        else:
            likelist.worklogs.add(worklog)

        # 좋아요 개수 계산
        like_count = worklog.like_count

        # 좋아요 개수를 응답 데이터에 추가
        return Response({'like_count': like_count}, status=HTTP_200_OK)
