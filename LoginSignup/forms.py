from django import forms
from LoginSignup.models import UserPrfoile


class UserProfileForm(forms.ModelForm):
    ProfilePicture = forms.ImageField(required=False)

    class Meta:
        model = UserPrfoile
        exclude = 'user'

