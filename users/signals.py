from django.db.models.signals import post_save
from .models import User
from django.dispatch import receiver
from feeds.models import Feed
from wallets.models import Wallet 



@receiver(post_save, sender=User)
def create_wallet(sender, instance, created, **kwargs):
    if created:
        Wallet.objects.create(owner = instance,)

@receiver(post_save, sender=User)
def create_feed(sender, instance, created, **kwargs):
    if created:
        Feed.objects.create(user = instance,)
