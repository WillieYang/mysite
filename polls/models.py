from django.db import models
import datetime
class Question(models.Model):
	question_text = models.CharField(max_length = 200)	
	public_date = models.DateTimeField('date published')

	def __unicode__(self):
		return self.question_text

	def was_published_recently(self):
		return self.public_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
	question = models.ForeignKey(Question)
	choice_text = models.CharField(max_length = 200)
	votes = models.IntegerField(default = 0)

	def __unicode__():
		return self.choice_text