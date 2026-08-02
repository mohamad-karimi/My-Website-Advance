from django.db.models.signals import post_save
from django.conf import settings
from django.dispatch import receiver
from .models import Profile

# Signals
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_or_update_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()