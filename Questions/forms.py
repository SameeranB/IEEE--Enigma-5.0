from django import forms
from django.contrib.auth.models import User
from .models import Achievement, QuestionInfo, UserProgress


class AnswerForm(forms.ModelForm):
    class Meta:
        model = UserProgress
        fields = {'Answer': 'CurrentAnswer'}


