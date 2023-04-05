from django.db import models
from common.models import CommonModel

class Follow(CommonModel):
    follower = models.ForeignKey("users.User", on_delete=models.CASCADE, related_name="following")
    followee = models.ForeignKey("users.User", on_delete=models.CASCADE, related_name="followers")

    class Meta:
        unique_together = ('follower', 'followee')
        verbose_name = "팔로우 관리"
        verbose_name_plural = "팔로우 목록 관리"

    def __str__(self):
        return f"{self.follower} follows {self.followee}"
