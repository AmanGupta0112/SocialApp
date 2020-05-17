from django.db import models
from django.urls import reverse,reverse_lazy
from django.conf import  settings
from misaka import *
from django.utils import timezone

from groups.models import GroupMember,Group
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your models here.

class Post(models.Model):
    user = models.ForeignKey(User,related_name='posts',on_delete=models.CASCADE)
    created_at =models.DateTimeField(default = timezone.now)
    message = models.TextField()
    message_html = models.TextField(editable=False)
    group = models.ForeignKey(Group,related_name='posts',on_delete=models.CASCADE)
    like = models.ManyToManyField(User,through='Liked',blank=True)

    def __str__(self):
        return self.message

    def save(self,*args,**kwargs):
        self.message_html=(self.message)
        super().save(*args,**kwargs)

    def get_absolute_url(self):
        return reverse('posts:single',kwargs={'username':self.user.username,'pk':self.pk})


class Comment(models.Model):
    post = models.ForeignKey('posts.Post',related_name='comments',on_delete=models.CASCADE)
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def __str__(self):
        return self.text

class Liked(models.Model):
    post = models.ForeignKey(Post,related_name='liking',on_delete=models.CASCADE)
    user = models.ForeignKey(User,related_name='user_posts',on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

    class Meta:
        unique_together=('post','user')
