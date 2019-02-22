from Questions.models import Achievements
from django_postgres_extensions.models.functions import *
from Questions.models import QuestionInfo

def rank_check(user, hint):
    ques = QuestionInfo.objects.get(QID__exact=user.CurrentQuestion)
    obj = ques.QuesSolved


    if obj <= 20:
        pointsscored = 100

    elif obj>20 and obj<=50:
        pointsscored = 80

    elif obj>50 and obj<=100:
        pointsscored = 60

    else:
        pointsscored = 50


    if hint == "True":
        pointsscored = pointsscored/2

    user.Points += pointsscored
    ques.QuesSolved += 1

    return pointsscored


def logger(req, type):
    if type = 1:
        obj = logs
    else: