# from django.core.checks import messages
from django.contrib import messages
from django.shortcuts import render
from groups.models import Group,GroupMember
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin
from django.urls import reverse
from django.views import generic
from django.shortcuts import get_object_or_404

# Create your views here.

class CreateGroup(LoginRequiredMixin,generic.CreateView):
    fields = ('name','discription')
    model = Group

class SingleGroup(generic.DetailView):
    model = Group

class ListGroup(generic.ListView):
    model = Group

class JoinGroup(LoginRequiredMixin,generic.RedirectView):

    def get_redirect_url(self, *args, **kwargs):
        return reverse('groups:single',kwargs= {'slug': self.kwargs.get('slug')})

    def get(self, request, *args, **kwargs):
        group = get_object_or_404(Group,slug = self.kwargs.get('slug'))

        try:
            GroupMember.objects.create(user =self.request.user,group = group)
        except :
            messages.warning(self.request,'Warning! Already a member.')
        else:
            messages.success(self.request,'You are a member now !')
        return super().get(request,*args,**kwargs)

class LeaveGroup(LoginRequiredMixin,generic.RedirectView):

    def get_redirect_url(self, *args, **kwargs):
        return reverse('groups:single',kwargs= {'slug': self.kwargs.get('slug')})

    def get(self, request, *args, **kwargs):
        try:
            membership = GroupMember.objects.filter(
                user= self.request.user,
                group__slug = self.kwargs.get('slug'),
            ).get()
        except GroupMember.DoesNotExist:
            messages.warning(self.request,'Your are not the member of this group!')
        else:
            membership.delete()
            messages.success(self.request,'You have left the group successfully!')
        return super().get(request,*args,**kwargs)
