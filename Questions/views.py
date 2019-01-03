from django.shortcuts import render
from django.views.generic import TemplateView, View, FormView
from django.http import HttpResponseRedirect, HttpResponse
from Questions.forms import AnswerForm
from Questions.models import QuestionInfo, Achievement, UserProgress
from django.contrib.auth.models import User
from django.urls import reverse


# Create your views here.

class QuestionView(FormView):

    template_name = 'Questions/Current_Question.html'
    form_class = AnswerForm

    def form_valid(self, form):
        user_answer = form.cleaned_data['Answer']
        if user_answer in QuestionInfo.Answer.objects.filter(QID=(self.request.user.achievements.Questions_Completed + 1)):
            return  HttpResponseRedirect(reverse("Questions/Question_Correct.html"))
        elif user_answer in QuestionInfo.CloseAnswer.objects.filter(QID=(self.request.user.achievements.Questions_Completed + 1)):
            return HttpResponse("You're Close")

    def get_context_data(self, **kwargs):
        question_info = QuestionInfo.objects.filter(QID__exact=self.request.user.progress.CurrentQuestion)
        context = super().get_context_data(**kwargs)
        context['Image'] = question_info.Image
        context['Question'] = question_info.QText
        context['AnswerForm'] = AnswerForm
        return context

class DashboardView(TemplateView):

    template_name = 'Questions/Dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['username'] = self.request.user.username
        context['fname'] = self.request.user.first_name
        context['lname'] = self.request.user.last_name
        context['mail'] = self.request.user.email
        return context




def under_development(request):
    return render(request, 'Under_Development.html')

