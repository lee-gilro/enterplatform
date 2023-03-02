from django.db import models
from common.models import CommonModel
from adminpage.baseAdmin import BaseAdmin

class Review(CommonModel):

    user = models.ForeignKey("users.User", on_delete=models.CASCADE, related_name="reviews")
    feed = models.ForeignKey("feeds.Feed", on_delete=models.CASCADE, related_name="reviews")
    payload = models.CharField(max_length=200,)
    class Meta:
        verbose_name = "댓글관리 관리"
        verbose_name_plural = "댓글 목록 관리"
    def __str__(self) -> str:
        return f"{self.user}:{self.payload}"
