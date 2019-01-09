from django.shortcuts import render
from django.views.generic import TemplateView, View, FormView
from django.http import HttpResponseRedirect, HttpResponse
from Questions.forms import AnswerForm
from Questions.models import QuestionInfo
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class QuestionView(LoginRequiredMixin, FormView):

    template_name = 'Questions/Current_Question.html'
    form_class = AnswerForm

    # Login-Required Settings:
    login_url = '/LoginSignup/Login'
    raise_exception = True
    redirect_unauthenticated_users = True

    def form_valid(self, form):
        user_answer = form.cleaned_data['Answer']
        if user_answer in QuestionInfo.Answer.objects.filter(QID__exact=self.request.user.CurrentQuestion):
            return  HttpResponseRedirect(reverse("Questions/Question_Correct.html"))
        elif user_answer in QuestionInfo.CloseAnswer.objects.filter(QID__exact=self.request.user.CurrentQuestion):
            return HttpResponse("You're Close")

    def get_context_data(self, **kwargs):
        question_info = QuestionInfo.objects.filter(QID__exact=self.request.user.CurrentQuestion)
        context = super().get_context_data(**kwargs)
        context['Image'] = question_info.Image
        context['Question'] = question_info.QText
        context['AnswerForm'] = AnswerForm
        return context

class DashboardView(LoginRequiredMixin, TemplateView):

    template_name = 'Questions/Dashboard.html'

    # Login-Required Settings:
    login_url = '/LoginSignup/Login'
    raise_exception = True
    redirect_unauthenticated_users = True


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['username'] = self.request.user.username
        context['fname'] = self.request.user.first_name
        context['lname'] = self.request.user.last_name
        context['mail'] = self.request.user.email
        return context




def under_development(request):
    return render(request, 'Under_Development.html')

