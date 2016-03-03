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

def profile(request):
	logged_in = request.session.get('logged_in', False)
	if not logged_in:
		return HttpResponseRedirect(reverse('GJ_app:login'))
	print "Logging in " + str(logged_in)
	print request.session.get('email')
	usr = get_object_or_404(User, email=request.session.get('email'))
	print usr
	company = get_object_or_404(Company,company_id = usr)
	print company

	if request.method == 'POST':
		Company.objects.filter(company_id=usr).update(company_name=request.POST['comp_name'])
		User.objects.filter(email=request.session.get('email')).update(email=request.POST['comp_email'])
		Company.objects.filter(company_id=usr).update(main_phone=request.POST['comp_phone'])
		Company.objects.filter(company_id=usr).update(main_address=request.POST['comp_address'])
		Company.objects.filter(company_id=usr).update(main_city=request.POST['comp_city'])
		Company.objects.filter(company_id=usr).update(main_state=request.POST['comp_state'])
		Company.objects.filter(company_id=usr).update(credit_number=request.POST['credit_num'])
		Company.objects.filter(company_id=usr).update(credit_expiration=request.POST['credit_expdate'])
		Company.objects.filter(company_id=usr).update(credit_zipcode=request.POST['credit_zipcode'])
		Branch.objects.filter(company_id=usr).update(branch_phone=request.POST['comp_phone'])
		Branch.objects.filter(company_id=usr).update(branch_address=request.POST['comp_address'])
		Branch.objects.filter(company_id=usr).update(branch_city=request.POST['comp_city'])
		Branch.objects.filter(company_id=usr).update(branch_state=request.POST['comp_state'])


	#usr = get_object_or_404(User.objects.all())
	#print usr
	return render(request, 'GJ_app/profile.html', {'usr' : usr, 'company':company})
		
def signup(request):
	#user = get_object_or_404(User)
	print User.objects.all()
	print Branch.objects.all()
	if request.method == 'POST':
		compname = request.POST['comp_name']
		compemail = request.POST['comp_email']
		comppassword = request.POST['comp_password']
		compphone = request.POST['comp_phone']
		compaddress = request.POST['comp_addr']
		compcity = request.POST['comp_city']
		compstate = request.POST['comp_state']
		compzip = request.POST['comp_zip']
		numbranch = request.POST['comp_branch_num']
		credname = request.POST['credit_holder']
		crednum = request.POST['credit_number']
		credexpdate = request.POST['credit_exp_date']
		credcvv = request.POST['credit_cvv']
		credzipcode = request.POST['credit_zip']
		print "password is " + comppassword
		print compname + " " + compemail + " " + comppassword + " " + compphone + " " + compaddress + " " + compcity + " " + compstate + " " +  compzip + " " + numbranch
		u = User(company_name=compname, email=compemail, password=comppassword)
		u.save()
		b = Branch(company_id=u, branch_phone=compphone, branch_address=compaddress, branch_city=compcity, branch_state=compstate, branch_zipcode=compzip)
		print "This branch"
		print  b
		b.save()
		c = Company(company_id=u, company_name=compname, main_phone=compphone, 
			main_address=compaddress, main_city=compcity, main_state=compstate, 
			main_zipcode=compzip, credit_number=crednum, credit_expiration=credexpdate,
			credit_cvv=credcvv, credit_zipcode=credzipcode, )
		print "This Company"
		print c
		c.save()
		return render(request, 'GJ_app/signupsuccess.html')


	#print companyname
	return render(request, 'GJ_app/signup.html')
	
def login(request):
	logged_in = request.session.get('logged_in', False)
	if logged_in:
		return HttpResponseRedirect(reverse('GJ_app:profile'))
		
	if request.method == 'POST':
		email = request.POST['email']
		password = request.POST['password']
		print "email = " + email + "\npassword = " + password
		request.session['logged_in'] = True
		request.session['email'] = email
		k = User.objects.get(email=email)
		print k
		user_id = k.user_id
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
							'categories':{'Meat':{'containers':{'Burger':
								{'options':{'Cheese':{'locked':True},
									'Bacon':{'locked':False, 'extra_price':0.20},
									'Pickles':{'locked':False, 'extra_price':0.05}}}, 'Wrap':{}}},
							'Sides':{'containers':{'Fries':{}}},
							'Drinks':{'containers':{'small':{}, 'medium':{}, 'large':{}}}},
							'last update':'today', 'food count':36})

def data(request): 
	return HttpResponseRedirect(reverse('GJ_app:menu_json'))


	