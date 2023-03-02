from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.utils.safestring import mark_safe
from common.models import CommonModel
# Create your models here.


class Feed(CommonModel):
    """Feed model definition"""

    user = models.OneToOneField("users.User", on_delete=models.CASCADE, related_name="feeds",)
    payloads = models.TextField(max_length=300,)
    backgroundimage = models.ImageField(upload_to= 'images')
    on_public = models.BooleanField(default=True)
    feed_name = models.CharField(max_length=150, default="")
    #worklogs = models.ForeignKey("WorkLog", on_delete=models.SET_NULL, null= True, blank=True, related_name= "feeds",)
    class Meta:
        verbose_name = "피드 관리"
        verbose_name_plural = "피드 목록 관리"
    def __str__(self) -> str:
        return self.user.username
    
    def img_preview(self):
        return mark_safe(f'<img src = "{self.backgroundimage.url}" width = "300" />')

class WorkLog(CommonModel):

    #poster = models.ForeignKey("users.User", on_delete=models.CASCADE, related_name="worklogs",)
    posted_feed = models.ForeignKey("Feed", on_delete=models.CASCADE,related_name="worklogs",)
    payload = models.TextField(max_length=250,)
    is_shop = models.BooleanField(default=False)
    on_public = models.BooleanField(default=False)
    class Meta:
        verbose_name = "워크로그 관리"
        verbose_name_plural = "워크로그 목록 관리"
    
    def __str__(self) -> str:
        return self.payload


    

