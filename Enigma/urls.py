"""Enigma URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url, include
from LoginSignup import views
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView



urlpatterns = [
    url(r'admin/', admin.site.urls),
    url(r'^$', views.LoginView.as_view(), name='index'),
    url(r'^LoginSignup/', include('LoginSignup.urls')),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.activate, name='activate'),
    url(r'^incorrectly_sent/$', views.IncorrectSent.as_view(), name='IncorrectSent'),
    url(r'^regcounter/$', views.RegCounter.as_view(), name='RegCounter'),

    # url(r'^remindpeeps/$', views.SendRem, name='rem'),
    #
    # url(r'^Questions/', include('Questions.urls')),
    # url(r'^reset-password/$', PasswordResetView.as_view(),{'template_name': 'LoginSignup/reset/reset_password.html', 'post_reset_redirect': 'password_reset_done'}, name='reset_password'),
    # url(r'^reset-password/reset-password-done/$', PasswordResetDoneView.as_view(),{'template_name': 'LoginSignup/reset/reset_password_done.html'}, name='password_reset_done'),
    # url(r'^reset-password/password_reset_confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', PasswordResetConfirmView.as_view(),{'template_name': 'LoginSignup/reset/reset_password_confirm.html', 'post_reset_redirect': 'password_reset_complete'}, name='password_reset_confirm'),
    # url(r'^reset-password/reset-password-complete/$', PasswordResetCompleteView.as_view(),{'template_name': 'LoginSignup/reset/reset_password_complete.html'}, name='password_reset_complete'),
]
