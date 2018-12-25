from django import forms
from django.contrib.auth.models import User



class UserForm(forms.ModelForm):
    confirm_email_id = forms.EmailField(required=True)
    password = forms.CharField(widget=forms.PasswordInput())
    BotCatcher = forms.CharField(required=False, widget=forms.HiddenInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password')

    def clean(self):
        all_clean_data = super().clean()
        email = all_clean_data['email']
        confirm_email_id = all_clean_data['confirm_email_id']
        botcatcher = all_clean_data['BotCatcher']
        if len(botcatcher) > 0:
            raise forms.ValidationError("BOT CAUGHT")

        if email != confirm_email_id:
            raise forms.ValidationError("Email-IDs don't match!")


class LoginForm(forms.Form):
    Username = forms.CharField(max_length=200)
    Password = forms.CharField(widget=forms.PasswordInput())


