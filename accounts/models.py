from django.db import models
from django.contrib.auth import models
from django.db import models as mo
from django.dispatch import receiver
from django.db.models.signals import post_save

import PIL
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
from django.contrib.auth import get_user_model
User_O = get_user_model()
# Create your models here.

class User(models.User,models.PermissionsMixin):

    def __str__(self):
        return "@{}".format(self.username)



class Profile(mo.Model):
    user = mo.OneToOneField(User_O, on_delete =mo.CASCADE)
    image = mo.ImageField(default ='download.png' , upload_to='profile_pics')
    # image_thumbnail = ImageSpecField(source= 'image', processors = [ResizeToFill(150,150)],format='JPEG', options = {'quality':60})

    # image_thumbnail = ImageSpecField(source= 'image', processors = [ResizeToFill(500,250)],format='JPEG', options = {'quality':60})
    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        super(Profile, self).save(force_insert, force_update, using, update_fields)
