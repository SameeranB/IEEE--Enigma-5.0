from django.conf.urls import url
from . import views

app_name='LoginSignup'

urlpatterns=[
    url(r'^Signup/$',views.Signup,name='Signup'),
    url(r'Login/$',views.Login,name='Login'),
]