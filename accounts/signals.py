from django.db.models.signals import post_save
from django.contrib.auth.models import User
# from django.dispatch import receiver
from accounts.models import Profile
# @receiver(post_save, sender=User)
def create_user_profile(sender, instance, created=False, **kwargs):
    if created:
        Profile.objects.create(user=instance)
post_save.connect(create_user_profile, sender=User)


# @receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

post_save.connect(save_user_profile, sender=User)
# @receiver(post_save, sender=User)
# def create_user_profile(sender, **kwargs):
#     if kwargs['created']:
#          Profile.objects.create(user=kwargs['instance'])
#
# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     instance.profile.save()
