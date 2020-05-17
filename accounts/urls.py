from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views

app_name = 'accounts'

urlpatterns =[

    url(r'login/$',auth_views.LoginView.as_view(template_name = 'accounts/login.html'),name='login'),
    url(r'logout/$',auth_views.LogoutView.as_view(),name='logout'),
    url(r'profile/$',views.Profile,name='profile'),
    url(r'password-reset/$',auth_views.PasswordResetView.as_view(template_name = 'accounts/password_reset.html'),name='password_reset'),
    url(r'password-reset-confirm/<uidb64>/<token>/$',auth_views.PasswordResetConfirmView.as_view(template_name = 'accounts/password_reset_confirm.html'),name='password_reset_confirm'),
    url(r'password-reset/done/$',auth_views.PasswordResetDoneView.as_view(template_name = 'accounts/password_reset_done.html'),name='password_reset_done'),
    url(r'password-reset-complete/$',auth_views.PasswordResetCompleteView.as_view(template_name = 'accounts/password_reset_complete.html'),name='password_reset_complete'),
    url(r'signup/$',views.SignUp.as_view(),name='signup'),
]
