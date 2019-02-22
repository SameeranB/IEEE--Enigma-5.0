from django import forms
from users.models import CustomUser


class AnswerForm(forms.ModelForm):

    class Meta:
        model = CustomUser
        fields = ('Answer',)


    Answer = forms.CharField(widget=forms.Textarea, label='')
    HintUsed = forms.CharField(widget=forms.HiddenInput(attrs={'id': 'check'}), label='', required=False)

    def clean(self):
        ans = self.cleaned_data['Answer']
        print(ans)