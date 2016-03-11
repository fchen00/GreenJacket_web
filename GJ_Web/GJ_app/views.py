from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from django.core.urlresolvers import reverse
from django.http import JsonResponse
from django.contrib import messages
from datetime import *

from .models import *
from .menu_controller import *
from .helpers_controller import *

# Users

def index(request):
	logged_in = request.session.get('logged_in', False)
	if logged_in:
		comp_id = request.session.get("user_id")
		print comp_id
		return HttpResponseRedirect(reverse('GJ_app:menuHome', args=[comp_id]))
		
	return render(request, 'GJ_app/index.html')
	
	

def menuHome(request, comp_id):
	logged_in = request.session.get('logged_in', False)
	if logged_in:
	# if is_logged:'
	# im going to be using the user_id until we set uo the session
		user = User.objects.get(user_id = comp_id)
		thisUser = user.user_id
		company_name = user.company_name
		menu = Menu.objects.filter(menu_id = thisUser)
		items = []
		for item in menu:
			items.extend(Item.objects.filter(item_id = item.item_id))

		options = Option.objects.all()
		currentDate = date.today();
		continDate= date(currentDate.year + 1, currentDate.month, currentDate.day)
		return render(request, 'GJ_app/menus/index.html', {'items': items, 'comp_id':comp_id,  'companyName' : company_name, 'currentDate' : currentDate, 'continDate': continDate, 'options':options})
	
	return render(request, 'GJ_app/index.html')

	
def activateItem(request, itemID):
	# if is_logged:'
	# im going to be using the user_id until we set uo the session
	item = Menu.objects.get(item_id = itemID)
	item.item_isActive = True
	item.save()
	return HttpResponseRedirect(reverse('GJ_app:index'))
	
def deactivateItem(request, itemID):
	# if is_logged:'
	# im going to be using the user_id until we set uo the session
	item = Menu.objects.get(item_id = itemID)
	item.item_isActive = False
	item.save()
	return HttpResponseRedirect(reverse('GJ_app:index'))

	
def itemMainInfo(request, itemID):
	# if is_logged:'
	# im going to be using the user_id until we set uo the session
	if request.method == 'POST':
		nickName = request.POST['nickNameEdit']
		basePrice = request.POST['basePriceEdit']
		startDate = request.POST['startDateEdit']
		endDate = request.POST['endDateEdit']
		startTime = request.POST['startTimeEdit']
		endTime = request.POST['endTimeEdit']
		
	item = Menu.objects.get(item_id = itemID)
	item.item_nickname = nickName
	item.item_basePrice = int(float(basePrice)*100)
	item.item_startDate = datetime.strptime(startDate,  "%m-%d-%Y")
	item.item_endDate = datetime.strptime(endDate,  "%m-%d-%Y")
	item.item_startTime = datetime.strptime(startTime, "%I:%M %p")
	item.item_endTime = datetime.strptime(endTime, "%I:%M %p")
	item.save()
	return HttpResponseRedirect(reverse('GJ_app:index'))
	

def addItem(request, menu_id):
	# if is_logged:'
	# im going to be using the user_id until we set uo the session
	categories = Category.objects.all()
	categoryOptions= CategoryOption.objects.all()
	sizes = Size.objects.all()
	containers = Container.objects.all()
	
	return render(request, 'GJ_app/createItem.html', {'categories': categories, 'containers':containers, 'sizes': sizes, 'categoryOptions':categoryOptions})
		
def pricing(request):
	return render(request, "GJ_app/pricing.html")



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
	#print User.objects.all()
	#print Branch.objects.all()
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
		k = User.objects.get(email=email)
		
		if k:
			request.session['logged_in'] = True
			request.session['email'] = email
			user_id = k.user_id
			request.session['user_id'] = user_id
		
		return HttpResponseRedirect(reverse('GJ_app:index'))
	else:
		return render(request, 'GJ_app/index.html')
	
def logout(request):
	logged_in = request.session.get('logged_in', False)
	if not logged_in:
		return HttpResponseRedirect(reverse('GJ_app:login'))
	
	request.session['logged_in'] = False
	return render(request, 'GJ_app/index.html')

# Testing Braintree
import braintree
from braintree.test.nonces import Nonces


braintree.Configuration.configure(braintree.Environment.Sandbox,
                                  merchant_id="r9kd7wjtk8cngfpq",
                                  public_key="3k4tcgjpwp6pxtmb",
                                  private_key="a1f5495a400cb65e2d4b46d0846fa218")
                                  
def pay (request):
    if request.method == "GET":
        braintree_token = braintree.ClientToken.generate()
        print braintree_token
        return render (request, 'GJ_app/pay.html', {'braintree_token': braintree_token})
    elif request.method == "POST":
        nonce = request.POST['payment_method_nonce']
        result = braintree.Transaction.sale({
            "amount": "1.00",
            "payment_method_nonce": nonce,
            "options": {
              "submit_for_settlement": True
            }
        })
        print "\n\nresult is", result, "\n\n"
        return render (request, 'GJ_app/message.html', {'message':"Payment Received"})

# # Menu Data to App
def menu_json(request):
	# dictionary to return
	"""
	'categories': 
	{
		1423:
		{
			'id': 1423,
			'name': 'Meat',
			'mains':
			{
				25:
				{
					'id': 25,
					'name': 'Chicken',
					'containers':
					{
						48:
						{
							'id': 48,
							'name': 'Bread',
							'item': {'id': 47, 'name': 'Chicken Sandwich',
										'mains': {25: {'id': 25, 'name': 'Chicken'}}},
							'sizes':
							{
								72:
								{
									'id': 72,
									'name': 'regular',
									'price': 6.12,
									'options':
									{
										41:
										{
											'id': 41,
											'name': 'Cheese',
											'fixed': False,
											'extra_price': .05
										}
									}
								}
								
							}
						}
						65:
						{
							'id': 65,
							'name': 'Salad Bowl',
							'item': {'id': 67, 'name': 'Chicken Salad',
										'mains': {25: {'id': 25, 'name': 'Chicken'}, 27: {'id': 27, 'name': 'Lettuce'}}},
							'sizes':
							{
								13:
								{
									'id': 13,
									'name': 'regular',
									'price': 5.40,
									'options':
									{
										42:
										{
											'id': 42,
											'name': 'Shredded Cheese',
											'fixed': False,
											'extra_price': .05
										}	
									}
								},
								34:
								{
									'id': 34,
									'name': 'large',
									'price': 6.40,
									options:
									{
										42:
										{
											'id': 42,
											'name': 'Shredded Cheese',
											'fixed': False,
											'extra_price': .05
										}	
									}									
								}
							}
						}
					}
				}
			}
			
		}
	}	
	"""
	branch_id = request.GET.get('branch', -1)
	print branch_id
	branch = get_object_or_404(Branch, branch_id = branch_id)
	company = get_object_or_404(Company, id = branch.company_id.user_id)
	menu_table = get_list_or_404(Menu, menu_id = company.company_id)
	
	item_table = []
	menu_dict = {'company_id': company.company_id.user_id, 'company_name': company.company_name}
	menu_dict['categories'] = {}
		
	for menu_entry in menu_table:
		# going by category id and main option id
		new_item = get_object_or_404(Item, item_id = menu_entry.item_id)
		item_table.append(new_item)
		category = new_item.category_id
		container = new_item.container_id
		
		if not category.category_id in menu_dict['categories']:
			menu_dict['categories'][category.category_id] = {'id': category.category_id,
									'name': category.category_name,
									'mains': {}}
		
		mains_dict = menu_dict['categories'][category.category_id]['mains']
		mains_dict[new_item.id] = menu_entry.item_nickname
		"""
		if not container.container_id in container_dict:
			container_dict[container.container_id] = {'id': container.container_id,
									'name': container.container_name,
									'sizes':{}, 'items':{}}
		
		mains_dict[container.container_id]['mains'][new_item.id] = menu_entry.item_nickname
		"""	
		
	
	
	return JsonResponse(menu_dict)
	
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


	