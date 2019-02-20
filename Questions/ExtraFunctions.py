from Questions.models import Achievements
from django_postgres_extensions.models.functions import *
from Questions.models import QuestionInfo

def rank_check(user):
    QuestionInfo.objects.filter(QID__exact=user.CurrentQuestion).update(Solved=ArrayAppend('Solved', user.username))
    obj = QuestionInfo.objects.filter(QID__exact=user.CurrentQuestion).annotate(position=ArrayPosition('Solved', user.username))

    if obj<=20:
        user.Points += 100
        return 100
    elif obj>20 and obj<=50:
        user.Points += 80
        return 80
    elif obj>50 and obj<=100:
        user.Points +=60
        return 60
    else:
        user.Points +=50
        return 50

def achievement_check(user):
    if 3 not in user.Achievements:
        if user.AttemptLog[user.CurrentQuestion] <=10:
            user.Achievements.append(3)

    if 4 not in user.Achievements:
        pass

