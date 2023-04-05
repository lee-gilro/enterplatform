from django.db import models
from common.models import CommonModel
# Create your models here.


class LikeList(CommonModel):
    user = models.ForeignKey("users.User", on_delete=models.CASCADE, related_name="user_likelists")
    worklogs = models.ManyToManyField("feeds.WorkLog", related_name="liked_by", blank=True)

    def __str__(self) -> str:
        return str(self.user)
