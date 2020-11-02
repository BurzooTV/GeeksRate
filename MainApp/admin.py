from django.contrib import admin
from . import models


class ChoiceInline(admin.TabularInline):
    model = models.Choices
    extra = 4


@admin.register(models.Questions)
class QuestionsAdmin(admin.ModelAdmin):
    list_display = ['question_id', 'question_title', 'question_answer']
    inlines = [ChoiceInline]


@admin.register(models.Choices)
class ChoicesAdmin(admin.ModelAdmin):
    list_display = ['choice_question', 'choice_text']


@admin.register(models.ScoreBoard)
class ScoreBoardAdmin(admin.ModelAdmin):
    list_display = ['name', 'point']


@admin.register(models.XValue)
class XValueAdmin(admin.ModelAdmin):
    list_display = ['x_id', 'x_point']

