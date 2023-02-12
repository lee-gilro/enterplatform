from django.db import models
from common.models import CommonModel
from adminpage.baseAdmin import BaseAdmin

class Review(CommonModel):

    user = models.ForeignKey("users.User", on_delete=models.CASCADE, related_name="reviews")
    feed = models.ForeignKey("feeds.Feed", on_delete=models.CASCADE, related_name="reviews")
    payload = models.CharField(max_length=200,)
    
    def __str__(self) -> str:
        return f"{self.user}:{self.payload}"
