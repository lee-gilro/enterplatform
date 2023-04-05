from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.utils.safestring import mark_safe
from common.models import CommonModel
# Create your models here.


class Feed(CommonModel):
    """Feed model definition"""

    user = models.OneToOneField("users.User", on_delete=models.CASCADE, related_name="feeds",)
    payloads = models.TextField(max_length=300,)
    backgroundimage = models.ImageField(upload_to= 'images', blank= True, null= True)
    on_public = models.BooleanField(default=True)
    feed_name = models.CharField(max_length=150, default="")
    class Meta:
        verbose_name = "피드 관리"
        verbose_name_plural = "피드 목록 관리"
    def __str__(self) -> str:
        return self.user.email if self.user else ''
    
    def img_preview(self):
        return mark_safe(f'<img src = "{self.backgroundimage.url}" width = "300" />')

class WorkLog(CommonModel):

    posted_feed = models.ForeignKey("Feed", on_delete=models.CASCADE,related_name="worklogs",)
    payload = models.TextField(max_length=250,)
    is_shop = models.BooleanField(default=False)
    on_public = models.BooleanField(default=False)
    likelists = models.ManyToManyField("likelists.LikeList", related_name="liked_worklogs", blank=True)
    class Meta:
        verbose_name = "워크로그 관리"
        verbose_name_plural = "워크로그 목록 관리"
    
    def __str__(self) -> str:
        return self.payload
    @property
    def like_count(self):
        return self.likelists.count()


    

