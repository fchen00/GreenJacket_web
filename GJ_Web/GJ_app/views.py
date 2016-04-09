from django.shortcuts import render, get_object_or_404, get_list_or_404, render_to_response
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from django.core.urlresolvers import reverse
from django.http import JsonResponse
from django.contrib import messages
from datetime import *
from cryptography.fernet import Fernet

from .models import *
from .menu_controller import *
from .helpers_controller import *

# Users

def index(request):
	logged_in = request.session.get('logged_in', False)
	print "Login? " + str(logged_in)
	print ('GJ'.encode('hex'))
	if logged_in:
		comp_id = request.session.get("user_id")
		# print comp_id
		return HttpResponseRedirect(reverse('GJ_app:menuHome', args=[comp_id]))
 		# return HttpResponseRedirect(reverse('GJ_app:menuHome'))
 	elif request.method == 'POST':
 		email = request.POST['email']
 		password = request.POST['password']
 		# print "GOt the method Post " + email + " " + password
 		# print "email = " + email + "\npassword = " + password
 		k = User.objects.get(email=email)
 		psright = (k.password == password.encode('hex'))
		
 		if k and psright:
 			request.session['logged_in'] = True
 			request.session['email'] = email
 			user_id = k.user_id
 			request.session['user_id'] = user_id 			
			return HttpResponseRedirect(reverse('GJ_app:index'))
		else:
			return render(request, 'GJ_app/index.html', {'message': "Incorrect Username and Password, please enter the correct username and password"})
	else:	
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
		
		categories = []
		for i in items:
			if i.category_id not in categories:
				categories.append(i.category_id)
				
		print categories
		
		return render(request, 'GJ_app/menus/index.html', {'items': items, 'comp_id':comp_id,  'companyName' : company_name, 'currentDate' : currentDate, 'continDate': continDate, 'options':options, 'categories': categories})
	


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
	
	return render(request, 'GJ_app/createItem.html', {'comp_id':menu_id, 'categories': categories, 'containers':containers, 'sizes': sizes, 'categoryOptions':categoryOptions})
	

def createItem(request, menu_id):
	# if is_logged:'
	# im going to be using the user_id until we set uo the session
	options = []
	optionsIsFixed = []
	options_price = []
	if request.method == 'POST':
		nickName = request.POST['nickNameNew']
		# if nickName == 'd':
			# messages.info(request, 'You will need to change your password in one week.')
			# return HttpResponseRedirect(reverse('GJ_app:addItem', args=[menu_id]))
		basePrice = ((int(request.POST['basePriceNatural'])) * 100) + int(request.POST['basePriceFloat'])
		startDate = datetime.strptime(request.POST['startDateNew'],  "%m-%d-%Y")
		endDate = datetime.strptime(request.POST['endDateNew'],  "%m-%d-%Y")
		startTime = datetime.strptime(request.POST['startTimeNew'], "%I:%M %p")
		endTime = datetime.strptime(request.POST['endTimeNew'],   "%I:%M %p")
		mainCategory = request.POST['postCategory']
		mainIngredient = request.POST['postMainIngredient']
		mainContainer = request.POST['postContainer']
		mainSize = request.POST['postMainSize']
		
		mainCount = 1
		if 'mainCount' in request.POST:
			mainCount = request.POST['mainCount']
		
		mainSizePrice = ((int(request.POST['mainSizeNatural'])) * 100) + int(request.POST['mainSizeFloat'])


		
		
		
		
		options.append(mainIngredient)
		optionsIsFixed.append('main')
		options_price.append(0)
		
		# this is for optional ingredients
		optionalCounter = 1
		while True:
			if ('postIng-'+ str(optionalCounter)) in request.POST:
				options_temp = 'postIng-' + str(optionalCounter)
				isFixed_temp = 'itemIsFixed-' + str(optionalCounter)
				if ('ingPriceNatural-'+ str(optionalCounter)) in request.POST:
					price_temp = ((int(request.POST['ingPriceNatural-' + str(optionalCounter)])) * 100) + int(request.POST['ingPriceFloat-' + str(optionalCounter)])
				else:
					price_temp = 0
				options.append(str(request.POST[options_temp]))
				optionsIsFixed.append(str(request.POST[isFixed_temp]))
				options_price.append(price_temp)

				optionalCounter = optionalCounter + 1
			else:
				break
			
		print options
		print optionsIsFixed
		print options_price
		
		mealCounter = 1
		meal_options = []
		meal_sizes = []
		meal_price = []
		count_meal_arr = []
		while True:
			if ('postSideIng-'+ str(mealCounter)) in request.POST:
				sides_temp = 'postSideIng-' + str(mealCounter)
				sidesSize_temp = 'postSideSize-' + str(mealCounter)
				
				if ('countMeal-'+ str(optionalCounter)) in request.POST:
					count_meal = request.POST['countMeal-' + str(mealCounter)]
					count_meal_arr.append(count_meal)
				else:
					count_meal_arr.append(1)
					
				price_temp = ((int(request.POST['mealNatural-' + str(mealCounter)])) * 100) + int(request.POST['mealFloat-' + str(mealCounter)])

				
				meal_options.append(str(request.POST[sides_temp]))
				meal_sizes.append(str(request.POST[sidesSize_temp]))
				meal_price.append(price_temp)
			
				mealCounter = mealCounter + 1
			else:
				break
				
		print meal_options
		print meal_sizes
		print meal_price
		print count_meal_arr
		
		# TODO:
	# price for each sizes
	# adding different sizes to tables
	# fixing count problem with meal
		
		userObject = User.objects.get(user_id=int(menu_id))
		
		new_menu_item = Menu(menu_id=userObject, item_nickname = nickName, item_basePrice = basePrice, item_isActive = 1,  item_startDate = startDate, item_endDate = endDate, item_startTime = startTime, item_endTime = endTime)
		new_menu_item.save()
		lastItem = Menu.objects.filter(menu_id=menu_id).last()
		
		
		sizeObject = Size.objects.get(size_id = int(mainSize))
		new_size = ItemSize(item_id = new_menu_item, size_id = sizeObject, itemSizePrice = mainSizePrice, item_count = mainCount)
		new_size.save()
		
		
		sizeCounter = 1
		while True:
			if ('postAddSize-'+ str(sizeCounter)) in request.POST:
				additionalSize = 'postAddSize-' + str(sizeCounter)
				
				m = request.POST[additionalSize]
				print m
				
				additionalSizeCount = 1
				if ('additionalSizeCount-' + str(sizeCounter))  in request.POST:
					additionalSizeCount = request.POST['additionalSizeCount-' + str(sizeCounter)]
				
				additionalSizePrice = ((int(request.POST['addSizeNatural-' +  str(sizeCounter)])) * 100) + int(request.POST['addSizeFloat-' +  str(sizeCounter)])
				
				sizeObject = Size.objects.get(size_id = int(request.POST[additionalSize]))
				new_size = ItemSize(item_id = new_menu_item, size_id = sizeObject, itemSizePrice = additionalSizePrice, item_count = additionalSizeCount)
				new_size.save()

				sizeCounter = sizeCounter + 1
			else:
				break
		
		
		
	
		optionsString = ",".join(options)
		optionsFixedString = ",".join(optionsIsFixed)
		optionsPriceString = ",".join(str(x) for x in options_price)
		
		optionsArray = []
		for x, val in enumerate(meal_options):
			mealOptionsString = ''
			mealOptionsString = str(val) + '-' + str(meal_sizes[x])
			optionsArray.append(mealOptionsString)
			
		completeMealString = ",".join(optionsArray)
		mealPrice = ",".join(str(x) for x in meal_price)
		
		catObject = Category.objects.get(category_id = int(mainCategory))
		contObject = Container.objects.get(container_id = int(mainContainer))
		
		new_item_entry = Item(item_id = lastItem, category_id = catObject, container_id = contObject, options = optionsString, options_isFixed = optionsFixedString, options_price = optionsPriceString, item_mealOptions = completeMealString,  item_mealPrice = mealPrice )
		new_item_entry.save()
		
	return HttpResponseRedirect(reverse('GJ_app:index'))
			
			
def deleteItem(request, item_id):
	
	menuItem = Menu.objects.get(item_id = item_id)
	
	sizeObjects = ItemSize.objects.filter(item_id = menuItem)
	sizeObjects.delete()
	
	itemObject = Item.objects.get(item_id = menuItem)
	itemObject.delete()
	
	menuItem.delete()
	
	return HttpResponseRedirect(reverse('GJ_app:index'))

	
		
def updateItem(request, item_id):
	# if is_logged:'
	# im going to be using the user_id until we set uo the session
	categories = Category.objects.all()
	categoryOptions= CategoryOption.objects.all()
	sizes = Size.objects.all()
	containers = Container.objects.all()
	
	menuObject = Menu.objects.get(item_id = item_id)
	itemObject = Item.objects.get(item_id = menuObject)
	itemSizeObjects = ItemSize.objects.filter(item_id = menuObject)
	itemSizeCount = itemSizeObjects.count()
	
	return render(request, 'GJ_app/editItem.html', {'item_id': item_id, 'categories': categories, 'containers':containers, 'sizes': sizes, 'categoryOptions':categoryOptions, 'menuObject': menuObject, 'itemObject': itemObject, 'itemSizeObjects': itemSizeObjects, 'itemSizeCount': itemSizeCount})
	
	
def pricing(request):
	return render(request, "GJ_app/pricing.html")



def profile(request):
	logged_in = request.session.get('logged_in', False)
	if not logged_in:
		return HttpResponseRedirect(reverse('GJ_app:login'))
	# print "Logging in " + str(logged_in)
	# print request.session.get('email')
	usr = get_object_or_404(User, email=request.session.get('email'))
	# print usr
	company = get_object_or_404(Company,company_id = usr)
	# print company

	if request.method == 'POST':
		Company.objects.filter(company_id=usr).update(company_name=request.POST['comp_name'])
		User.objects.filter(email=request.session.get('email')).update(email=request.POST['comp_email'])
		Company.objects.filter(company_id=usr).update(main_phone=request.POST['comp_phone'])
		Company.objects.filter(company_id=usr).update(main_address=request.POST['comp_address'])
		Company.objects.filter(company_id=usr).update(main_city=request.POST['comp_city'])
		Company.objects.filter(company_id=usr).update(main_state=request.POST['comp_state'])
		

	#usr = get_object_or_404(User.objects.all())
	#print usr
	return render(request, 'GJ_app/profile.html', {'usr' : usr, 'company':company})
		
def signup(request):
	'''
	if request.method == 'POST':
		compname = request.POST['comp_name']
		compemail = request.POST['comp_email']
		comppassword = request.POST['comp_password']
		compphone = request.POST['comp_phone']
		compaddress = request.POST['comp_addr']
		compcity = request.POST['comp_city']
		compstate = request.POST['comp_state']
		compzip = request.POST['comp_zip']
		numbranches = request.POST['numBranch']
		print "password is " + comppassword
		print compname + " " + compemail + " " + comppassword + " " + compphone + " " + compaddress + " " + compcity + " " + compstate + " " +  compzip + " " + numbranches
		u = User(company_name=compname, email=compemail.lower(), password=comppassword, is_admin=False)
		u.save()
		c = Company(company_id=u, company_name=compname, main_phone=compphone, 
			main_address=compaddress, main_city=compcity, main_state=compstate, 
			main_zipcode=compzip, branches_category=numbranches, is_active=False)
		print "This Company"
		print c
		c.save()
		return render(request, 'GJ_app/signupsuccess.html')
	'''
	#print companyname

	if request.method == "GET":
		braintree_token = braintree.ClientToken.generate()
		# print braintree_token
		return render (request, 'GJ_app/signup.html', {'braintree_token': braintree_token})
	elif request.method == "POST":

		compname = request.POST['comp_name']
		compemail = request.POST['comp_email']
		comppassword = (request.POST['comp_password']).encode('hex')
		compphone = request.POST['comp_phone']
		compaddress = request.POST['comp_addr']
		compcity = request.POST['comp_city']
		compstate = request.POST['comp_state']
		compzip = request.POST['comp_zip']
		numbranches = request.POST['numBranch']
		# print "password is " + comppassword
		##Hexing the password


		# print compname + " " + compemail + " " + comppassword + " " + compphone + " " + compaddress + " " + compcity + " " + compstate + " " +  compzip + " " + numbranches
		u = User(company_name=compname, email=compemail.lower(), password=comppassword, is_admin=False)
		u.save()
		c = Company(company_id=u, company_name=compname, main_phone=compphone, 
			main_address=compaddress, main_city=compcity, main_state=compstate, 
			main_zipcode=compzip, branches_category=numbranches, is_active=False)
		# print "This Company"
		# print c
		c.save()


		nonce = request.POST['payment_method_nonce']
		result = braintree.Transaction.sale({
			"amount": "1.00",
			"payment_method_nonce": nonce,
			"options": {
			  "submit_for_settlement": True
			}
		})
		# print "\n\nresult is", result, "\n\n"
		
		return render(request, 'GJ_app/signupsuccess.html')
		#return render(request, 'GJ_app/signup.html', {'message':"Payment Received"})



'''
I think we can remove this since we can login through the index page
'''	
def login(request):
	logged_in = request.session.get('logged_in', False)
	if logged_in:
		return HttpResponseRedirect(reverse('GJ_app:profile'))
		
	if request.method == 'POST':
		email = request.POST['email']
		password = request.POST['password']
		# print "GOt the method Post " + email + " " + password
		# print "email = " + email + "\npassword = " + password
		k = User.objects.get(email=email.tolower())
		
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
	branch_id = request.GET.get('branch', "-1")
	
	if branch_id == "-1":
		branch_id = request.GET.get('company', "-1")
	
	if branch_id == "-1":
		return render (request, 'GJ_app/message.html', {'message':
			"Please send the branch id with the following syntax:\n"
			+ "/data/?branch={branch id}"})
	
	print "data for branch", branch_id
	#branch = get_object_or_404(Branch, branch_id = branch_id)
	#company = get_object_or_404(Company, id = branch.company_id.user_id)
	company = get_object_or_404(Company, id = branch_id)
	menu_table = get_list_or_404(Menu, menu_id = company.company_id)
	
	#print "branch is ", branch
	print "company is ", company
	
	item_table = []
	menu_dict = {'company_id': company.company_id.user_id, 'company_name': company.company_name}
	menu_dict['categories'] = {}
		
	for menu_entry in menu_table:
		# going by category id and main option id
		try:
			new_item = get_object_or_404(Item, item_id = menu_entry.item_id)
		except:
			print "Missing item in database with id:", menu_entry.item_id
			continue
		
		if (menu_entry.item_isActive == 0):
			print "Item", menu_entry.item_nickname, "is inactive: skipping"
			continue
			
		item_table.append(new_item)
		
		print "for", menu_entry.item_nickname, "in first half:"
		
		# Set categories in return JSON
		category = new_item.category_id
		if not category.category_id in menu_dict['categories']:
			menu_dict['categories'][category.category_id] = {'id': category.category_id,
									'name': category.category_name,
									'mains': {}}
		
		mains_dict = menu_dict['categories'][category.category_id]['mains']
		
		# Get Options and meals
		options_list = new_item.options.split(',')
		options_type = new_item.options_isFixed.split(',')
		options_price = new_item.options_price.split(',')
		options_data = []
		
		temp_meal_list = new_item.item_mealOptions.split(',')
		meal_prices = new_item.item_mealPrice.split(',')
		meal_options = []
		meal_sizes = []
		
		#print "options list is", options_list
		#print "options type is", options_type
		#print "options price is", options_price
		
		# Fix price
		for i, price_str in enumerate(options_price):
			temp_float = float(price_str)
			temp_out = "{:.2f}".format(temp_float/100)
			options_price[i] = temp_out
			
			try:
				options_data.append(get_object_or_404(Option, option_id = options_list[i]))
			except:
				print "Error, missing option with id:", options_list[i]
		
		
		for i, m_price_str in enumerate(meal_prices):
			try:
				temp_float = float(m_price_str)
			except:
				print "Missing meal item in database for item", new_item.id
				temp_float = 0
				continue
				
			temp_out = "{:.2f}".format(temp_float/100)
			meal_prices[i] = temp_out
			
			meal_options.append(temp_meal_list[i].split('-')[0])
			meal_sizes.append(temp_meal_list[i].split('-')[1])
			
		
		# populate Main Options in return json
		# requires only one main ingredient
		main_id  = None
		
		for i, opt_id in enumerate(options_list):
			if options_type[i] == "main":
				main_id = opt_id
				if not opt_id in mains_dict:
					mains_dict[opt_id] = {'id': opt_id, 
											'name': options_data[i].option_name,
											'containers': {}}
				
		
		container_dict = mains_dict[main_id]['containers']
		new_container = new_item.container_id
		container_dict[new_container.container_id] = {'id': new_container.container_id,
														'name': new_container.container_name, 'sizes':{}}
		
		sizes_dict = container_dict[new_container.container_id]['sizes']
		
		options_dicts = []
		meals_dicts = []
		
		#print "id is about to be", new_item.item_id.item_id
		try:
			new_size = get_list_or_404(ItemSize, item_id = new_item.item_id.item_id)
			for i, size_row in enumerate(new_size):
				temp_size_dict = {'id': size_row.id, 'name_id':size_row.size_id.size_id, 'name': size_row.size_id.size_name,
								'real_item': {'name': menu_entry.item_nickname, 'id': new_item.item_id.item_id,
								'is_active': menu_entry.item_isActive},
								#'count': size_row.item_count, 'price': size_row.itemSizePrice, 'options': {}}
								'count': size_row.item_count, 'price': "{:.2f}".format(float(size_row.itemSizePrice)/100),
								'options': {}, 'meals': {}}
				sizes_dict[size_row.id] = temp_size_dict
				options_dicts.append(temp_size_dict['options'])
				meals_dicts.append(temp_size_dict['meals'])
				
		except:
			print "size not found"
			temp_size_dict = {'id': 0, 'name_id':'         ERROR!!! SIZE MISSING!!!          ',
								'name': '            ERROR!!! SIZE MISSING!!!          ',
								'real_item': {'name': menu_entry.item_nickname, 'id': new_item.item_id.item_id,
												'is_active': menu_entry.item_isActive},
								'count': '0', 'price': '0', 'options': {}, 'meals': {}}
			sizes_dict['0'] = temp_size_dict
			options_dicts.append(temp_size_dict['options'])
			meals_dicts.append(temp_size_dict['meals'])
			
		
		for option_dict in options_dicts:
			for i, option in enumerate(options_list):
				if options_type[i] != 'main':
					option_dict[option] = {'id':option, 'name': options_data[i].option_name, 'type': options_type[i], 
											'price': options_price[i]}
		
		for meal_dict in meals_dicts:
			for j, meal_option in enumerate (meal_options):
				try:
					temp_option = get_object_or_404(Option, option_id = meal_option)
				except:
					print "Invalid option id:", meal_option,"from meal:"
					continue
				try:
					temp_size = get_object_or_404(Size, size_id = meal_sizes[j])
				except:
					print "Invalid size id:", meal_sizes[j],"from meal"
					continue
				
				meal_dict[meal_option] = {'id': meal_option, 'option_id': meal_option, 'size_id': meal_sizes[j],
											'price': meal_prices[j], 'size_name': temp_size.size_name,
											'count': 0, 'option_name': temp_option.option_name}
		
		#print options_dicts
		
		print
			
	return JsonResponse(menu_dict)

def data(request): 
	temp_id = request.GET.get('company', "-1")
	if temp_id == "-1":
		temp_id = request.GET.get('branch', "-1")
		
	return HttpResponseRedirect(reverse('GJ_app:menu_json') + '?company=' 
											+ temp_id)









'''
Example of Encrpytion

Preinstall
pip install cryptography
from cryptography.fernet import Fernet

Example:
>>> encrypted = 'H\xe7\n@\xe0\x13\xe0M\xc32\xce\x16@\xb2B\xd0'
>>> encoded = encrypted.encode('hex')
>>> decoded = encoded.decode('hex')
>>> encrypted == decoded
True
'''

	