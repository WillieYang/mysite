from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse

from .models import Question, Choice

def index(request):
	latest_question_list = Question.objects.order_by('public_date')[:5]
	context = {
		'latest_question_list': latest_question_list,
	}
	return render(request, 'polls/index.html', context)

def results(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	return render(request, 'polls/resuts.html', {'question': question})

def vote(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	try:
		selected_choice = question.choice_set.get(pk=request.POST['choice'])
	except (KeyError, Choice.DoesNotExist):
		return render(request, 'polls/detail.html', {
			'question': question,
			'error_message': "You didn't select a choice.",
			})
	else:
		selected_choice.votes += 1
		selected_choice.save()
		return HttpResponseRedirect(reverse('polls:result', args=(question.id,)))




def detail(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	return render(request, 'polls/detail.html', {'question': question})
