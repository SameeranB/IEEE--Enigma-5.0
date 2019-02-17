from django import forms
from django.core.exceptions import ValidationError
from django.core import validators

from users.models import CustomUser
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV3

class UserForm(forms.ModelForm):

    BotCatcher = forms.CharField(required=False, widget=forms.HiddenInput, label = '')
    class Meta:
        model = CustomUser
        fields = ('username', 'first_name','email', 'password', 'University')



    username = forms.CharField(widget=forms.TextInput(attrs={'id':'input-box','placeholder': 'Username'}), label='')
    first_name = forms.CharField(widget=forms.TextInput(attrs={'id': 'input-box', 'placeholder': 'Name'}), label='')
    email = forms.EmailField(widget=forms.TextInput(attrs={'id': 'input-box', 'placeholder': 'Email'}), label='',
                             validators=validators.EmailValidator())
    University = forms.CharField(widget=forms.TextInput(attrs={'id': 'input-box', 'placeholder': 'University / '
                                                                                                 'Organization'}),
                                 label='')
    password = forms.CharField(widget=forms.PasswordInput(attrs={'id': 'input-box', 'placeholder': 'Password'}), label='')
    captcha = ReCaptchaField(widget=ReCaptchaV3, label='')

    def clean(self):
        all_clean_data = super().clean()
        email = all_clean_data['email']
        botcatcher = all_clean_data['BotCatcher']

        if len(botcatcher) > 0:
            raise forms.ValidationError("BOT CAUGHT")

        exists = CustomUser.objects.filter(email=email)
        if exists:
            raise ValidationError("Email address %s has already registered, please check your inbox for the confirmation mail" % email)



class LoginForm(forms.Form):

    Username = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'id' : 'input-box', 'placeholder' : 'Username'}), label='')
    Password = forms.CharField(widget=forms.PasswordInput(attrs={'id' : 'input-box', 'placeholder' : 'Password'}), label='')


