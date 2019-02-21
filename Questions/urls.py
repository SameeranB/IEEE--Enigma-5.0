from django.conf.urls import url
from Questions import views

app_name= "Questions"

urlpatterns=[
    url(r'^QuestionSolver/$',views.QuestionView.as_view(), name='Question_Solver'),
    url(r'^Dashboard/$', views.DashboardView.as_view(), name='Dashboard'),
    url(r'^UnderDevelopment/$', views.UnderDevelopment.as_view(), name='Under_Dev'),
    url(r'^Achievements/$', views.AllAchievements.as_view(), name='Achievements'),
    url(r'^Achievements/(?P<pk>[-\w+])/$', views.AchievementDetail.as_view(), name='Achievement_Details'),
    url(r'^Leaderboard/$', views.Leaderboard.as_view(), name='Leaderboard'),
    url(r'^Story/$', views.StoryView.as_view(), name='Story'),

]
