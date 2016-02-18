from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from django.core.urlresolvers import reverse
from django.http import JsonResponse

from .models import Question

# Users
def index(request):
	latest_question_list = Question.objects.order_by('-pub_date')[:5]
	context = {
		'latest_question_list': latest_question_list,
		}
	return render(request, 'GJ_app/index.html',context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'GJ_app/detail.html', {'question': question})


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'GJ_app/results.html', {'question':question})

def vote(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	try:
		selected_choice = question.choice_set.get(pk=request.POST['choice'])
	except (keyError, Choice.DoesNotExists):
		return render(request,'GJ_app/details.html', {'question':question, 'error_message':"You didn't select a choice.",})
	else:
		selected_choice.votes +=1
		selected_choice.save()
    	return HttpResponseRedirect(reverse('GJ_app:results', args=(question.id,)))

def signup(request):
	return render(request, 'GJ_app/signup.html')
	
def login(request):
	if request.method == 'POST':
		print "username = " + request.POST['username'] + "\npassword = " + request.POST['password']
		return HttpResponseRedirect(reverse('GJ_app:index'))
	else:
		return render(request, 'GJ_app/login.html')
	
def logout(request):
	return render(request, 'GJ_app/logout.html')

# Menu Data to App
def menu_json(request):
	return JsonResponse({'restaurant name':'Cafe One', 'restaurant id':1746928, 
							'menu':{'foods':[{'burger':{'options':['cheese', 'pickels']}}, 
												{'sandwich':{'options':['chicken', 'bacon', 'blt']}}]},
							'last update':'today', 'food count':36})

def data(request): 
	return HttpResponseRedirect(reverse('GJ_app:menu_json'))
	