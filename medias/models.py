from django.db import models
from common.models import CommonModel
# Create your models here.

class Photo(CommonModel):

    file = models.ImageField()
    description = models.CharField(max_length=140,)
    worklog = models.ForeignKey(
        "feeds.WorkLog", 
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="photos"
    )

    def __str__(self) -> str:
        return "Photo File"

class Video(CommonModel):

    file = models.FileField()
    worklog = models.ForeignKey(
        "feeds.WorkLog",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="videos",
    )
    
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
    
    def __str__(self) -> str:
        return self.title