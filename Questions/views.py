from django.shortcuts import render

from django.views.generic import TemplateView,FormView, ListView

from ratelimit.mixins import RatelimitMixin

from Questions.forms import AnswerForm, AnswerHintForm
from Questions.models import QuestionInfo
from django.contrib.auth.mixins import LoginRequiredMixin
from Questions.models import Story
from users.models import CustomUser
from .ExtraFunctions import rank_check, logger

# Create your views here.


class QuestionView(LoginRequiredMixin, FormView):

    template_name = 'Questions/Current_Question.html'
    form_class = AnswerForm

    # Login-Required Settings:
    login_url = '/LoginSignup/Login'
    raise_exception = False
    redirect_unauthenticated_users = True
    Attempts = 0
    Dist = 0


    def form_valid(self, form):

        user_answer = form.cleaned_data['Answer']
        logger(self.request, 1, form.cleaned_data['Answer'], "QuestionView")

        profile = CustomUser.objects.get(username=self.request.user.username)
        self.Attempts += 1
        profile.save()
        question = QuestionInfo.objects.filter(QID__exact=self.request.user.CurrentQuestion)
        user_answer = user_answer.lower()

        if user_answer in question[0].Answer:
            pointsscored = rank_check(profile)
            profile.CurrentQuestion +=1
            # achievement_check(profile)

            profile.save()
            return render(self.request, 'Questions/Question_Correct.html', context={'scored':pointsscored, 'Hint': self.request.user.TimeLog})
        elif user_answer in question[0].CloseAnswer:
            self.Dist = 1
        elif user_answer in question[0].MediumAnswer:
            self.Dist = 2
        else:
            self.Dist = 3

        return render(self.request, 'Questions/Current_Question.html', {'Image': question[0].Image, 'Question': question[0].QText, 'AnswerForm': AnswerForm, 'Attempts': self.Attempts, 'Dist': self.Dist})



    def get_context_data(self, **kwargs):
        question_info = QuestionInfo.objects.filter(QID__exact=self.request.user.CurrentQuestion)
        context = super().get_context_data(**kwargs)
        context['Image'] = question_info[0].Image
        context['Question'] = question_info[0].QText
        context['AnswerForm'] = AnswerForm
        context['Attempts'] = self.Attempts
        context['Dist'] = self.Dist
        context['Trig'] = False
        context['Name'] = self.request.user.username
        context['Score'] = self.request.user.Points

        return context



# After Hint The Following Is Used

class QuestionAfterHintView(LoginRequiredMixin, FormView):

    template_name = 'Questions/Current_Question.html'
    form_class = AnswerHintForm

    # Login-Required Settings:
    login_url = '/LoginSignup/Login'
    raise_exception = False
    redirect_unauthenticated_users = True
    Attempts = 0
    Dist = 0


    def form_valid(self, form):

        user_answer = form.cleaned_data['Answer']
        logger(self.request, 1, form.cleaned_data['Answer'], "QuestionView")

        profile = CustomUser.objects.get(username=self.request.user.username)
        self.Attempts += 1
        profile.save()
        question = QuestionInfo.objects.filter(QID__exact=self.request.user.CurrentQuestion)
        user_answer = user_answer.lower()

        if user_answer in question[0].Answer:
            pointsscored = rank_check(profile)
            profile.CurrentQuestion +=1
            # achievement_check(profile)

            profile.save()
            return render(self.request, 'Questions/Question_Correct.html', context={'scored':pointsscored, 'Hint': self.request.user.TimeLog})
        elif user_answer in question[0].CloseAnswer:
            self.Dist = 1
        elif user_answer in question[0].MediumAnswer:
            self.Dist = 2
        else:
            self.Dist = 3

        return render(self.request, 'Questions/Current_Question.html', {'Image': question[0].Image, 'Question': question[0].QText, 'AnswerForm': AnswerForm, 'Attempts': self.Attempts, 'Dist': self.Dist, 'Hint': question[0].Hints[0]})



    def get_context_data(self, **kwargs):
        question_info = QuestionInfo.objects.filter(QID__exact=self.request.user.CurrentQuestion)
        context = super().get_context_data(**kwargs)
        context['Image'] = question_info[0].Image
        context['Question'] = question_info[0].QText
        context['AnswerForm'] = AnswerHintForm
        context['Attempts'] = self.Attempts
        context['Dist'] = self.Dist
        context['Trig'] = True
        context['Hint'] = question_info[0].Hints[0]
        context['Name'] = self.request.user.username
        context['Score'] = self.request.user.Points
        profile = CustomUser.objects.get(username=self.request.user.username)
        profile.TimeLog = True
        profile.save()
        return context





#
# class DashboardView(LoginRequiredMixin, TemplateView):
#
#     template_name = 'Questions/Dashboard.html'
#
#     # Login-Required Settings:
#     login_url = '/'
#     raise_exception = False
#     redirect_unauthenticated_users = True
#
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['username'] = self.request.user.username
#         context['fname'] = self.request.user.first_name
#         context['lname'] = self.request.user.last_name
#         context['mail'] = self.request.user.email
#         return context


class UnderDevelopment(TemplateView):
    template_name = 'Under_Development.html'


# class AllAchievements( LoginRequiredMixin, ListView):
#     login_url = '/'
#     raise_exception = False
#     redirect_unauthenticated_users = True
#
#     context_object_name = 'AllAchievements'
#     model = Achievements
#     template_name = 'Questions/All_Achievements.html'
#
#     # def get(self, request, *args, **kwargs):
#     #     collected = request.user.Achievements
#     #     return HttpResponse(collected)
#
#
# class AchievementDetail(DetailView):
#     login_url = '/'
#     raise_exception = False
#     redirect_unauthenticated_users = True
#
#     context_object_name = 'AchievementDetail'
#     model = Achievements
#     template_name = 'Questions/Achievement_Detail.html'


class Leaderboard(LoginRequiredMixin, ListView):

    ratelimit_key = 'ip'
    ratelimit_rate = '10/m'
    ratelimit_block = True
    ratelimit_method = 'GET'


    login_url = '/'
    raise_exception = False
    redirect_unauthenticated_users = True

    queryset = CustomUser.objects.order_by('-Points', '-Achievements')[:100]
    context_object_name = 'Leaderboard'
    template_name = 'Questions/Leaderboard.html'



    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Name'] = self.request.user.username
        context['Score'] = self.request.user.Points
        logger(self.request, 1, "", "Leaderboard")
        return context


class StoryView(LoginRequiredMixin, ListView):
    login_url = '/'
    raise_exception = False
    redirect_unauthenticated_users = True

    context_object_name = 'StoryList'
    def get_queryset(self):
        return Story.objects.filter(SID__lt=self.request.user.CurrentQuestion).order_by('SID')
    template_name = 'Questions/story.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Name'] = self.request.user.username
        context['Score'] = self.request.user.Points
        logger(self.request, 1, "", "Story")
        return context



class LogView(ListView):
    context_object_name = 'Logged'

    def get_queryset(self):
        obj = Story.objects.all().values_list('username', flat=True)
