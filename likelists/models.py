from django.db import models
from common.models import CommonModel
# Create your models here.


class LikeList(CommonModel):

    user = models.ForeignKey("users.User", on_delete=models.CASCADE, related_name="likelists",)
    worklogs = models.ForeignKey("feeds.WorkLog", on_delete=models.CASCADE, related_name= "likelists",)

    def __str__(self) -> str:
        return self.user