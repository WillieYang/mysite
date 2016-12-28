from django.contrib import admin

from .models import Question

class QuestionAdmin(admin.ModelAdmin):
	fields = ['public_date', 'question_text']
		
admin.site.register(Question, QuestionAdmin)
