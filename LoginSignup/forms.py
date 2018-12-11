from django import forms
from LoginSignup.models import UserProfile
from django.contrib.auth.models import User


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password')


class UserProfileForm(forms.ModelForm):
    ProfilePicture = forms.ImageField(required=False)

    class Meta:
        model = UserProfile
        exclude = 'user'

