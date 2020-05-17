from django.contrib import admin
from posts.models import Post,Comment,Liked
# Register your models here.

admin.site.register(Post)
admin.site.register(Comment)

class PostLikedInline(admin.TabularInline):
    model = Liked
