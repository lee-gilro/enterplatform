from django.db.models.signals import post_save
from .models import User
from django.dispatch import receiver

from wallets.models import Wallet 
import secrets


@receiver(post_save, sender=User)
def create_wallet(sender, instance, created, **kwargs):
    if created:
        Wallet.objects.create(owner = instance,)
