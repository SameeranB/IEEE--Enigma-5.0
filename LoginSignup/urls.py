from django.conf.urls import url, include
from LoginSignup import views



app_name= "LoginSignup"

urlpatterns=[

    url(r'^Signup/$', views.signup_view, name='Signup'),
    url(r'^Login/$', views.LoginView.as_view(), name='Login'),
    url(r'^Logout/$', views.LogoutView.as_view(), name='Logout'),
    url(r'NotConf/$', views.NotConf.as_view(), name='NotConf')


]
