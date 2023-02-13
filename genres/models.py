from django.db import models
from common.models import CommonModel

class Genre(CommonModel):
    name = models.CharField(max_length=100,)
    description = models.TextField()

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name_plural = "Categories"

class Artist(CommonModel):
    name = models.CharField(max_length=100,)
    description = models.TextField()
    genres = models.ManyToManyField("Genre")
    image = models.ImageField()

    def __str__(self) -> str:
        return self.name

