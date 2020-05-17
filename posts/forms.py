from django import forms
from posts.models import Post,Comment

class PostFrom(forms.ModelForm):

    class Meta:
        # ordering =['-created_at']
        model = Post
        fields = ('message','group')

class CommentForm(forms.ModelForm):

    class Meta():
        ordering = ['-id']
        model = Comment
        fields = ('author','text')
