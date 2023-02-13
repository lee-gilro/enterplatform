from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    class GenderChoices(models.TextChoices):
        MALE = ("male","Male")
        FEMALE = ("female","Female")
    class LanguageChoices(models.TextChoices):
        KR = ("kr","Korean")
        EN = ("en", "English")
    class CurrencyChoices(models.TextChoices):
        WON = "won", "Korean Won"
        USD = "usd", "Dollar"
    nickname = models.CharField(max_length=150, default="",)
    is_artist = models.BooleanField(default=False)
    email = models.EmailField(blank=True, null=True)
    avatar = models.URLField(blank=True) # default 로 회색 화면 설정필요
    gender = models.CharField(max_length=10, choices=GenderChoices.choices,)
    language = models.CharField(max_length=2, choices=LanguageChoices.choices,)
    currency = models.CharField(max_length=5, choices=CurrencyChoices.choices,)
    point = models.FloatField(max_length=5, verbose_name="assets", default= 0)
    country = models.CharField(max_length=50, default="KOR")
    address = models.CharField(max_length=200, default="")
    is_curated = models.BooleanField(default=False)