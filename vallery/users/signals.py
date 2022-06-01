from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

from vallery.users.models import Profile, User


@receiver(pre_save, sender=User)
def generate_id(sender, instance, **kwargs):
    """Generate id for user.

    Args:
        sender: User model.
        instance: User instance.
        **kwargs: Keyword arguments.

    """
    if not instance.id:
        instance.id, _ = instance.generate_address()


@receiver(post_save, sender=User)
def create_and_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        # BlockChainAddress.objects.create(user=instance)
    # Profile.objects.filter(user=instance).update(**kwargs)


# @receiver(pre_save, sender=BlockChainAddress)
# def generate_address(sender, instance, **kwargs):
#     if not instance.address:
#         instance.generate_address()
