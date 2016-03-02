from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from django.core.urlresolvers import reverse
from datetime import date

from .models import *

# we have to define 

def index(request, comp_id):
	# if is_logged:'
	# im going to be using the user_id until we set uo the session
	user = User.objects.get(user_id = comp_id)
	thisUser = user.user_id
	company_name = user.company_name
	menus = Menu.objects.filter(menu_id = thisUser)
	currentDate = date.today();
	continDate= date(currentDate.year + 1, currentDate.month, currentDate.day)
	return render(request, 'GJ_app/menus/index.html', {'menus': menus, 'companyName' : company_name, 'currentDate' : currentDate, 'continDate': continDate})

	

	
# def editInfo(request):
		# if(request.GET.get('mybtn')):
		# .mypythonfunction( int(request.GET.get('mytextbox')) )
	# return render_to_response('myApp/templateHTML.html')

	
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