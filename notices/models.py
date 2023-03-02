from django.db import models
from common.models import CommonModel

class Notice(CommonModel):
    title = models.CharField(max_length=100)
    img = models.ImageField()
    context = models.TextField()
    creator = models.ForeignKey("users.User",on_delete=models.CASCADE)
    class Meta:
        verbose_name = "공지사항 관리"
        verbose_name_plural = "공지사항 목록 관리"

class Faq(CommonModel):
    question = models.CharField(max_length=150)
    img = models.ImageField()
    answer = models.TextField()
    creator = models.ForeignKey("users.User", on_delete=models.CASCADE)
    class Meta:
        verbose_name = "FAQ 관리"
        verbose_name_plural = "FAQ 목록 관리"