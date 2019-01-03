from django.conf.urls import url
from Questions import views

app_name= "Questions"

urlpatterns=[
    url(r'^QuestionSolver/$',views.QuestionView.as_view(), name='Question_Solver'),
    url(r'^Dashboard/$', views.DashboardView.as_view(), name='Dashboard'),
    url(r'^UnderDevelopment/$', views.under_development, name='Under_Dev'),
]
