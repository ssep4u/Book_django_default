from django.contrib import admin
from .models import Question, Choice


class ChoiceInlne(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date infromantion', {'fields':['pub_date']}),
    ]

    list_display = ('question_text', 'pub_date', 'was_published_recently')

    inlines = [ChoiceInlne]

    list_filter = ['pub_date']
    search_fields = ['question_text']

admin.site.register(Question, QuestionAdmin)