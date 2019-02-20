from django.shortcuts import render
from django.views.generic import TemplateView,FormView, ListView, DetailView
from django.http import HttpResponse
from Questions.forms import AnswerForm
from Questions.models import QuestionInfo
from django.contrib.auth.mixins import LoginRequiredMixin
from Questions.models import Achievements
from users.models import CustomUser
from .ExtraFunctions import achievement_check, rank_check
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
        profile = self.request.user
        profile.AttemptLog += 1
        profile.save()

        question = QuestionInfo.objects.filter(QID__exact=self.request.user.CurrentQuestion)

        if user_answer in question[0].Answer:
            pointsscored = rank_check(profile)
            profile.CurrentQuestion += 1
            profile.AttemptLog = 0
            achievement_check(profile)

            profile.save()
            return render(self.request, 'Questions/Question_Correct.html', context={'scored':pointsscored})
        elif user_answer in question[0].CloseAnswer:
            return HttpResponse("You're Close")
        else:
            return HttpResponse("Nahh...Try Again")

    def get_context_data(self, **kwargs):
        question_info = QuestionInfo.objects.filter(QID__exact=self.request.user.CurrentQuestion)
        context = super().get_context_data(**kwargs)
        context['Image'] = question_info[0].Image
        context['Question'] = question_info[0].QText
        context['AnswerForm'] = AnswerForm
        context['Attempts'] = self.request.user.AttemptLog
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


class UnderDevelopment(TemplateView):
    template_name = 'Under_Development.html'


class AllAchievements(ListView):
    context_object_name = 'AllAchievements'
    model = Achievements
    template_name = 'Questions/All_Achievements.html'

    # def get(self, request, *args, **kwargs):
    #     collected = request.user.Achievements
    #     return HttpResponse(collected)


class AchievementDetail(DetailView):
    context_object_name = 'AchievementDetail'
    model = Achievements
    template_name = 'Questions/Achievement_Detail.html'


class Leaderboard(ListView):
    context_object_name = 'Leaderboard'
    model = CustomUser
    template_name = 'Questions/Leaderboard.html'
    ordering = ['Points']





# class QuestionMakerList(ListView):
#     context_object_name = 'AllQuestions'
#     model = QuestionInfo
#     template_name = 'Questions/AllQuestions.html'
#     ordering = ['QID']
#
# class QuestionMakerDetail(DetailView):
#     context_object_name = 'QuestionDetail'
#     model = QuestionInfo
#     template_name = 'Questions/Question_Detail.html'