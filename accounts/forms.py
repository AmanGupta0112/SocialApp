from django.contrib.auth import models
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Profile
class UserCreateForm(UserCreationForm):

    class Meta():
        fields = ('username','email','password1','password2')
        model = models.User

        # def __init__(self,*args,**kwargs):
        #     super().__init__(*args,**kwargs)
        #     self.fields['username'].labels = 'Display Name'
        #     self.fields['email'].labels = 'Email Address'

class UserUpdateForm(forms.ModelForm):
    class Meta():
        model = models.User
        fields = ['username','email']

class ProfileUpdateForm(forms.ModelForm):
    class  Meta():
        model = Profile
        fields = ['image']
