from django.conf.urls import url
from posts import views

app_name='posts'

urlpatterns =[
    url(r'^$',views.ListPost.as_view(),name='all'),
    url(r'new/',views.CreatePost.as_view(),name='create'),
    url(r'^by/(?P<username>[-\w]+)/$',views.UserPost.as_view(),name='for_user'),
    url(r'^by/(?P<username>[-\w]+)/(?P<pk>\d+)/$',views.PostDetail.as_view(),name='single'),
    url(r'^delete/(?P<pk>\d+)/$',views.DeletePost.as_view(),name='delete'),
    url(r'^update/(?P<pk>\d+)/$',views.UpdatePost.as_view(),name='update'),
    url(r'^comment/(?P<pk>\d+)/$',views.add_comment_to_post,name='comment'),
    url(r'^delete_comment/(?P<pk>\d+)/$',views.comment_remove,name='delete_comment'),
    url(r'^postlike/(?P<pk>\d+)/$',views.PostLikeView.as_view(),name='Like'),
    url(r'^postdislike/(?P<pk>\d+)/$',views.DislikeView.as_view(),name='Dislike'),
]
