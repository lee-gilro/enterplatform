from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import NotFound
from rest_framework.status import HTTP_200_OK
from .models import LikeList
from .serializers import LikeListSerializer
from feeds.models import WorkLog

class LikeLists(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):
        likelist = LikeList.objects.filter(user = request.user)
        serializer = LikeListSerializer(
            likelist,
            many = True,
          
        )
        return Response(serializer.data)
    

class LikeListToggle(APIView):
    def get_list(self, pk, user):
        try:
            return LikeList.objects.get(pk=pk, user=user)  # 누구의 feed 에 몇번째 worklog 인지
        except LikeList.DoesNotExist:
            raise NotFound
        
    def get_worklog(self, pk):
        try:
            return WorkLog.objects.get(pk=pk)
        except WorkLog.DoesNotExist:
            raise NotFound
        
    def put(self, request, pk, worklog_pk):
        likelist = self.get_list(pk, request.user)
        worklog = self.get_worklog(worklog_pk)

        if likelist.worklogs.filter(pk=worklog.pk).exists():
            likelist.worklogs.remove(worklog)
        else:
            likelist.worklogs.add(worklog)
        return Response(status=HTTP_200_OK)