from django.conf.urls import url
from . import views

app_name='LoginSignup'

urlpatterns=[
    url(r'^Signup/$',views.signup_view,name='Signup'),
    # url(r'Login/$',views.login_view,name='Login'),
]