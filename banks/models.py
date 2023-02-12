from django.db import models
from common.models import CommonModel



class Bank(CommonModel):
    bankname = models.CharField(max_length=50,)
    bankcode = models.CharField(max_length=50,)

    def __str__(self) -> str:
        return f"{self.bankname}({self.bankcode})"