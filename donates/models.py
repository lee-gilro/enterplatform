from django.db import models
from common.models import CommonModel


class Donate(CommonModel):
    from_user = models.ForeignKey("users.User", on_delete=models.PROTECT, related_name="donates_from_user")
    to_user = models.ForeignKey("users.User", on_delete=models.PROTECT,related_name="donates_to_user")
    amount = models.IntegerField()
    content = models.CharField(max_length=150, null= True, blank= True)
    class Meta:
        verbose_name = "후원 관리"
        verbose_name_plural = "후원 목록 관리"
    def __str__(self) -> str:
        return f"from {self.from_user} to {self.to_user}"