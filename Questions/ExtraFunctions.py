from Questions.models import Achievements



def achievement_check(user):
    if 3 not in user.Achievements:
        if user.AttemptLog[user.CurrentQuestion] <=10:
            user.Achievements.append(3)

    if 4 not in user.Achievements:
        pass

