from .models import OrganizationProfile, Organization
from django.dispatch import receiver
from django.db.models.signals import post_save


@receiver(post_save, sender=Organization)
def create_profile_singal(sender, instance, created, **kwargs):
    if created:
        org_profile = OrganizationProfile(organization=instance)
        org_profile.save()
