from django.contrib import admin

from QA.models import Question, Answer


class QuestionAdmin(admin.ModelAdmin):
    list_display = ['text', 'is_deleted', 'date_created', 'date_updated']


class AnswerAdmin(admin.ModelAdmin):
    list_display = ['text', 'is_deleted', 'date_created', 'date_updated']


admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer, AnswerAdmin)
