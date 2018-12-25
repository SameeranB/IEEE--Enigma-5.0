from django import forms
from django.contrib.auth.models import User
from .models import Achievement, Question


class AddQuestionForm(forms.Form):
    class Meta:
        model = Question
        fields = '__all__'

