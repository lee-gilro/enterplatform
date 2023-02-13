from django.db import models
from common.models import CommonModel


class Tutorial(CommonModel):
    name = models.CharField(max_length=100, )
    description = models.TextField(max_length=300,)
    image = models.ImageField()

class Curation(CommonModel):
    text = models.TextField(max_length=300,)
    