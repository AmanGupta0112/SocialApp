from django.shortcuts import render,get_object_or_404,redirect
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse,reverse_lazy
from django.views import generic
from django.http import Http404
from braces.views import SelectRelatedMixin
from . import models
from . import forms
from django.contrib.auth.decorators import login_required
# from posts.models import Post
# from . import forms
from django.contrib.auth import get_user_model
User = get_user_model()
# Create your views here.

class ListPost(LoginRequiredMixin,generic.ListView):
    model = models.Post
    select_related = ('user','group')

class UserPost(generic.ListView):
    model = models.Post
    template_name = 'posts/user_post_list.html'

    def get_queryset(self):
        try:
            self.post_user = User.objects.prefetch_related('posts').get(username__iexact=self.kwargs.get('username'))
        except User.DoesNotExist:
            raise Http404
        else:
            return  self.post_user.posts.all()

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['post_user']=self.post_user
        return context


class PostDetail(SelectRelatedMixin,generic.DetailView):
    model = models.Post
    select_related = ('user','group')

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user__username__iexact=self.kwargs.get('username'))

class CreatePost(LoginRequiredMixin,SelectRelatedMixin,generic.CreateView):
     fields = ('group','message')
     model = models.Post
     redirect_field_name = 'posts/post_form.html'

     def form_valid(self, form):
        self.object=form.save(commit=False)
        self.object.user= self.request.user
        self.object.save()
        return super().form_valid(form)

class DeletePost(LoginRequiredMixin,SelectRelatedMixin,generic.DeleteView):
    model = models.Post
    select_related = ('user','group')
    success_url = reverse_lazy('posts:all')

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user_id=self.request.user.id)


    def delete(self, *args, **kwargs):
        messages.success(self.request,'Post Deleted')
        return super().delete(*args,**kwargs)

class UpdatePost(generic.UpdateView,LoginRequiredMixin,SelectRelatedMixin):
    model = models.Post
    fields = ('group', 'message')
    redirect_field_name = 'posts/post_detail.html'

    def form_valid(self, form):
       self.object=form.save(commit=False)
       self.object.user= self.request.user
       self.object.save()
       return super().form_valid(form)

@login_required
def add_comment_to_post(request,pk):
        post =get_object_or_404(models.Post,pk=pk)
        if request.method == 'POST':
            form = forms.CommentForm(request.POST)

            if form.is_valid():
                comment = form.save(commit=False)
                comment.post = post
                comment.save()
                return redirect('posts:all')
        else:
            form = forms.CommentForm()
        return render(request,'posts/comment_form.html',{'form':form})

@login_required
def comment_remove(request,pk):
    comment = get_object_or_404(models.Comment,pk = pk)
    post_pk = comment.post.pk
    comment.delete()
    return  redirect('posts:all')

class PostLikeView(LoginRequiredMixin,generic.RedirectView):

    def get_redirect_url(self,*args,**kwargs):
        return reverse('posts:all')
    # id = models.Post.objects.filter(id)
    def get(self,request,*args,**kwargs):

        post= get_object_or_404(models.Post,pk=self.kwargs.get('pk'))

        try:
            models.Liked.objects.create(user = self.request.user, post = post)
        except:
            messages.warning(self.request,'Warning! Already liked.')
        else:
            messages.success(self.request,'Thanks!')

        return super().get(request,*args,**kwargs)

class DislikeView(LoginRequiredMixin,generic.RedirectView):

    def get_redirect_url(self,*args,**kwargs):
        return reverse('posts:all')

    def get(self,request,*args,**kwargs):

        try:
            liking = models.Liked.objects.filter(
                user=self.request.user,
                post_id = self.kwargs.get('pk')
                # post__pk =  self.kwargs.get('pk')
            ).get()
        except models.Liked.DoesNotExist:
            messages.warning(self.request,'Post Cant Be Liked!')
        else:
            liking.delete()
            messages.success(self.request,'Disliked')
        return super().get(request,*args,**kwargs)
