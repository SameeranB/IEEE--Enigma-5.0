from django import forms
from LoginSignup.models import UserProfile
from django.contrib.auth.models import User


class UserForm(forms.ModelForm):
    confirm_email_id = forms.EmailField(required=True)
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password')

    def clean(self):
        all_clean_data = super().clean()
        email = all_clean_data['email']
        confirm_email_id = all_clean_data['confirm_email_id']

        if email != confirm_email_id:
            raise forms.ValidationError("Email-IDs don't match!")


class UserProfileForm(forms.ModelForm):
    ProfilePicture = forms.ImageField(required=False)
    BotCatcher = forms.CharField(required=False, widget=forms.HiddenInput)

    class Meta:
        model = UserProfile
        exclude = ('user',)

    def clean(self):
        all_clean_data = super().clean()
        botcatcher = all_clean_data['BotCatcher']
        if len(botcatcher) > 0:
            raise forms.ValidationError("BOT CAUGHT")
