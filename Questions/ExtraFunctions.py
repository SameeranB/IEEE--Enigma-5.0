from datetime import timezone, datetime

from Questions.models import Achievements
from django_postgres_extensions.models.functions import *
from Questions.models import QuestionInfo
from LoginSignup.models import logs
from ipware import get_client_ip

def rank_check(user):
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


    if user.TimeLog:
        pointsscored = pointsscored/2

    user.Points += pointsscored
    ques.QuesSolved += 1
    ques.save()
    user.TimeLog = False
    user.Achievements = datetime.now()
    user.save()

    return pointsscored


def logger(req, type, ans, VN):
    if type == 1:
        obj = logs()
        obj.username = req.user.username
        obj.IPAdd = get_client_ip(req)
        obj.AnswerSub = ans
        obj.TimeStamp = datetime.now()
        obj.ViewName = VN
        obj.save()
    else:
        obj = logs()
        obj.IPAdd = get_client_ip(req)
        obj.TimeStamp = datetime.now()
        obj.save()