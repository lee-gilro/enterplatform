from django.db import models
from common.models import CommonModel



class Bank(CommonModel):
    bankname = models.CharField(max_length=50,)
    bankcode = models.CharField(max_length=50,)
    class Meta:
        verbose_name = "연결은행"
        verbose_name_plural = "연결 은행 목록"

    def __str__(self) -> str:
        return f"{self.bankname}({self.bankcode})"
    