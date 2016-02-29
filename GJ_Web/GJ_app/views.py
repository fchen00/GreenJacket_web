from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from django.core.urlresolvers import reverse
from django.http import JsonResponse

from .models import *
from .menu_controller import *
from .helpers_controller import *

# Users

def index(request):
	# menus = Menu.objects.all()
	# for i in menus:
		# print i.menu_id.user_id
	return render(request, 'GJ_app/index.html')

# def detail(request, question_id):
    # question = get_object_or_404(Question, pk=question_id)
    # return render(request, 'GJ_app/detail.html', {'question': question})


# def results(request, question_id):
    # question = get_object_or_404(Question, pk=question_id)
    # return render(request, 'GJ_app/results.html', {'question':question})

# def vote(request, question_id):
	# question = get_object_or_404(Question, pk=question_id)
	# try:
		# selected_choice = question.choice_set.get(pk=request.POST['choice'])
	# except (keyError, Choice.DoesNotExists):
		# return render(request,'GJ_app/details.html', {'question':question, 'error_message':"You didn't select a choice.",})
	# else:
		# selected_choice.votes +=1
		# selected_choice.save()
    	# return HttpResponseRedirect(reverse('GJ_app:results', args=(question.id,)))

		
def signup(request):
	return render(request, 'GJ_app/signup.html')
	
def login(request):
	logged_in = request.session.get('logged_in', False)
	if logged_in:
		return HttpResponseRedirect(reverse('GJ_app:index'))
		
	if request.method == 'POST':
		email = request.POST['email']
		password = request.POST['password']
		print "email = " + email + "\npassword = " + password
		request.session['logged_in'] = True
		request.session['email'] = email
		request.session['user_id'] = user_id
		
		return HttpResponseRedirect(reverse('GJ_app:index'))
	else:
		return render(request, 'GJ_app/login.html')
	
def logout(request):
	logged_in = request.session.get('logged_in', False)
	if not logged_in:
		return HttpResponseRedirect(reverse('GJ_app:login'))
	
	request.session['logged_in'] = False
	return render(request, 'GJ_app/logout.html')

# Menu Data to App
def menu_json(request):
	return JsonResponse({'restaurant name':'Cafe One', 'restaurant id':1746928, 
							'menu':{'foods':[{'burger':{'options':['cheese', 'pickels']}}, 
												{'sandwich':{'options':['chicken', 'bacon', 'blt']}}]},
							'last update':'today', 'food count':36})

def data(request): 
	return HttpResponseRedirect(reverse('GJ_app:menu_json'))
	