from django.db import models
from common.models import CommonModel

class Genre(CommonModel):
    name = models.CharField(max_length=100,)
    description = models.TextField()

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = "장르 관리"
        verbose_name_plural = "장르 목록 관리"

class Artist(CommonModel):
    name = models.CharField(max_length=100,)
    description = models.TextField()
    genres = models.ManyToManyField("Genre")
    image = models.ImageField()
    class Meta:
        verbose_name = "참조 아티스트 관리"
        verbose_name_plural = "참조 아티스트 목록 관리"
    def __str__(self) -> str:
        return self.name

