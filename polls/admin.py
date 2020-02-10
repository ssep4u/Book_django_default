from django.contrib import admin
from .models import Question, Choice


class ChoiceInlne(admin.StackedInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date infromantion', {'fields':['pub_date']}),
    ]
    inlines = [ChoiceInlne]

admin.site.register(Question, QuestionAdmin)