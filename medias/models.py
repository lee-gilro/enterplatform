from django.db import models
from django.utils.safestring import mark_safe
from common.models import CommonModel
# Create your models here.

class Photo(CommonModel):

    file = models.ImageField(upload_to= 'images', blank=False, null=False)
    description = models.CharField(max_length=140,)
    worklog = models.ForeignKey(
        "feeds.WorkLog", 
        on_delete=models.CASCADE,
        related_name="photos"
    )
    class Meta:
        verbose_name = "이미지 관리"
        verbose_name_plural = "이미지 목록 관리"

    def __str__(self) -> str:
        return "Photo File"
    
    def img_preview(self): #new
        return mark_safe('<img src = "{url}" width = "300"/>'.format(
             url = self.file.url
         ))
    
class Video(CommonModel):

    file = models.FileField()
    worklog = models.ForeignKey(
        "feeds.WorkLog",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="videos",
    )
    class Meta:
        verbose_name = "비디오 관리"
        verbose_name_plural = "비디오 목록 관리"
    def __str__(self) -> str:
        return "Video File"

class Music(CommonModel):
    title = models.CharField(max_length=150,)
    description = models.TextField()
    ganres =models.ManyToManyField("genres.Genre", related_name="musics")
    file = models.FileField()
    worklog = models.ForeignKey(
        "feeds.Feed",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="musics",
    )
    class Meta:
        verbose_name = "음원 관리"
        verbose_name_plural = "음원 목록 관리"
    def __str__(self) -> str:
        return self.title