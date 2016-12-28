from django.contrib import admin

from .models import Question, Choice

class QuestionAdmin(admin.ModelAdmin):
	fieldsets = [
		('Questions:', {'fields': ['question_text']}),
		('Date information', {'fields':['public_date'], 'classes':
			['collapse']}),
	]
		
admin.site.register(Question, QuestionAdmin)

admin.site.register(Choice)
