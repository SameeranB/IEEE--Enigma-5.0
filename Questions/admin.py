from django.contrib import admin
from Questions.models import QuestionInfo, Achievements, Story, EasterEggs

# Register your models here.

admin.site.register(QuestionInfo)
admin.site.register(Achievements)
admin.site.register(Story)