from django import forms
from users.models import CustomUser


class AnswerForm(forms.ModelForm):

    class Meta:
        model = CustomUser
        fields = ('Answer',)


    Answer = forms.CharField(widget=forms.Textarea, label='')
