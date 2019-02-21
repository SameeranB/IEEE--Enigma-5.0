from Questions.models import Achievements
from django_postgres_extensions.models.functions import *
from Questions.models import QuestionInfo

def rank_check(user):
    ques = QuestionInfo.objects.get(QID__exact=user.CurrentQuestion)
    obj = ques.QuesSolved

    if obj<=20:
        user.Points += 100
        ques.QuesSolved += 1
        return 100
    elif obj>20 and obj<=50:
        user.Points += 80
        ques.QuesSolved += 1
        return 80
    elif obj>50 and obj<=100:
        user.Points +=60
        ques.QuesSolved += 1
        return 60
    else:
        user.Points +=50
        ques.QuesSolved += 1
        return 50
