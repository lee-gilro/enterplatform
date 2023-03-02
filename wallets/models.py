from django.db import models
from common.models import CommonModel

# Create your models here.



class Wallet(CommonModel):
    class PaymentKindChoices(models.TextChoices):
        CREDIT_CARD = ("credit_card", "Credit Card")
        GOOGLE_PLAYSTORE = ("google_play_store", "Google Play Store")
        APPLE_STORE = ("apple_store", "apple store")
        PAYPAL =("paypal", "Paypal")

    owner = models.ForeignKey("users.User", on_delete= models.CASCADE, blank=True, null= True)
    payment_method = models.CharField(max_length=20, choices=PaymentKindChoices.choices, blank=True,null=True)
    bisou = models.FloatField(default=0)
    bank = models.ForeignKey("banks.Bank", on_delete=models.SET_NULL, null= True, blank= True)
    account = models.CharField(max_length=200, default= "", blank= True, null= True)
    class Meta:
        verbose_name = "지갑 관리"
        verbose_name_plural = "지갑 목록 관리"
    def __str__(self) -> str:
        return f"{self.owner}'s wallet"