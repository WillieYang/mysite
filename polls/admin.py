from django.contrib import admin
from .models import Question, Choice

class ChoiceInline(admin.TabularInline):
	model = Choice
	extra = 3

class QuestionAdmin(admin.ModelAdmin):
	fieldsets = [
		('Questions:', {'fields': ['question_text']}),
		('Date information', {'fields':['public_date'], 'classes':
			['collapse']}),
	]
	inlines = [ChoiceInline]
	list_display = ('question_text', 'public_date', 'was_published_recently')
	list_filter = ['public_date']
	search_fields = ['question_text']

admin.site.register(Question, QuestionAdmin)

