from django.shortcuts import render
from django.views.generic import TemplateView, View, FormView
from .forms import AddQuestionForm
from django.http import HttpResponseRedirect

# Create your views here.


class AddQuestionView(FormView):
    template_name = 'Questions/AddQuestion.html'
    success_url = 'Questions/ListQuestions.html'
    form_class = AddQuestionForm

    def form_valid(self, form):
        form.save(commit=True)
        return HttpResponseRedirect(reversed('Questions/ListQuestions.html'))

