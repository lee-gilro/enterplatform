from django.db import models
from django.contrib.postgres.fields import ArrayField
from common.models import CommonModel
# Create your models here.


class Feed(CommonModel):
    """Feed model definition"""

    user = models.OneToOneField("users.User", on_delete=models.CASCADE, related_name="feeds",)
    payloads = models.TextField(max_length=300,)
    backgroundimage = models.ImageField()
    on_public = models.BooleanField(default=True)
    feed_name = models.CharField(max_length=150, default="")
    #worklogs = models.ForeignKey("WorkLog", on_delete=models.SET_NULL, null= True, blank=True, related_name= "feeds",)
    def __str__(self) -> str:
        return self.user.username

class WorkLog(CommonModel):

    #poster = models.ForeignKey("users.User", on_delete=models.CASCADE, related_name="worklogs",)
    posted_feed = models.ForeignKey("Feed", on_delete=models.CASCADE,)
    payload = models.TextField(max_length=250,)
    is_shop = models.BooleanField(default=False)
    on_public = models.BooleanField(default=False)
    
    def __str__(self) -> str:
        return self.payload


    

