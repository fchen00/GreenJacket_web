# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    company_name = models.CharField(max_length=200)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=1000)
    QR_code = models.BinaryField(db_column='QR_code', blank=True, null=True)  # Field name made lowercase.
    is_admin = models.NullBooleanField()

    def __str__(self):        
        return self.company_name + " " + self.email + " " + str(self.user_id) + " " + self.password + " " + str(self.is_admin)

    class Meta:
        managed = False
        db_table = 'User'
		
	def __init__(self, user_id, company_name, email, password, qr_code, is_admin):
		self.user_id = user_id
		self.company_name = company_name
		self.email = email
		self.password = password
		self.QR_code = QR_code_code
		self.is_admin = is_admin
	
	# def __repr__(self):
	# 	return '<User %r, %r, %r>' % self.name, self.company_name, self.is_admin

class Branch(models.Model):
    branch_id = models.AutoField(primary_key=True)
    company_id = models.ForeignKey(User, db_column='company_id', on_delete=models.CASCADE)
    branch_phone = models.CharField(max_length=12, blank=True, null=True)
    branch_address = models.CharField(max_length=200, blank=True, null=True)
    branch_city = models.CharField(max_length=200, blank=True, null=True)
    branch_state = models.TextField(blank=True, null=True)  # This field type is a guess.
    branch_zipcode = models.TextField(blank=True, null=True)  # This field type is a guess.
    date_added = models.DateField(auto_now_add=True, blank=True)

    def __str__(self):
    	return self.company_id.company_name + " " + self.branch_phone + " " + self.branch_address + "," + self.branch_city + "," + self.branch_state + "," + self.branch_zipcode + " " + str(self.date_added)

    class Meta:
        managed = False
        db_table = 'Branch'


class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):        
        return str(self.category_id) + " 	" + self.category_name

    class Meta:
        managed = False
        db_table = 'Category'

class Option(models.Model):
    option_id = models.AutoField(primary_key=True)
    option_name = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return str(self.option_id) + " " + self.option_name
    class Meta:
        managed = False
        db_table = 'Option'

class CategoryOption(models.Model):
    id = models.AutoField(primary_key=True)  
    category_id = models.ForeignKey(Category, db_column='category_id', on_delete=models.CASCADE)
    option_id = models.ForeignKey(Option, db_column='option_id', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id) + " " + str(self.category_id.category_id) + " " + str(self.option_id.option_id)

    class Meta:
        managed = False
        db_table = 'Category-Option'


class Company(models.Model):
    id = models.AutoField(primary_key=True)  # AutoField?
    company_id = models.ForeignKey(User, db_column='company_id', on_delete=models.CASCADE)
    company_name = models.CharField(max_length=200)
    main_phone = models.TextField(blank=True, null=True)  # This field type is a guess.
    main_address = models.CharField(max_length=200, blank=True, null=True)
    main_city = models.CharField(max_length=200, blank=True, null=True)
    main_state = models.TextField(blank=True, null=True)  # This field type is a guess.
    main_zipcode = models.TextField(blank=True, null=True)  # This field type is a guess.
    credit_holder = models.TextField(blank=True, null=True)
    credit_number = models.TextField(blank=True, null=True)  # This field type is a guess.
    credit_expiration = models.TextField(blank=True, null=True)  # This field type is a guess.
    credit_cvv = models.CharField(max_length=4, blank=True, null=True)
    credit_zipcode = models.TextField(blank=True, null=True)  # This field type is a guess.
    date_created = models.DateField(auto_now_add=True, blank=True)
    last_updated = models.DateField(blank=True, null=True)
    is_active = models.NullBooleanField()

    def __str__(self):        
        return self.company_id.company_name + " " + self.main_phone + " " + self.main_address + "," + self.main_city + "," + self.main_state + "," + self.main_zipcode

    class Meta:
        managed = False
        db_table = 'Company'


class Container(models.Model):
    container_id = models.AutoField(primary_key=True)
    container_name = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return str(self.container_id) + " " + self.container_name

    class Meta:
        managed = False
        db_table = 'Container'

class Menu(models.Model):
	item_id = models.AutoField(primary_key=True)
	menu_id = models.ForeignKey(User, db_column='menu_id', on_delete=models.CASCADE)
	item_nickname = models.CharField(max_length=200)
	item_basePrice = models.IntegerField(db_column='item_basePrice')  # Field name made lowercase.
	item_isActive = models.NullBooleanField(db_column='item_isActive')  # Field name made lowercase.
	item_startDate = models.DateField(db_column='item_startDate', blank=True, null=True)  # Field name made lowercase.
	item_endDate = models.DateField(db_column='item_endDate', blank=True, null=True)  # Field name made lowercase.
	item_startTime = models.TimeField(db_column='item_startTime', blank=True, null=True)
	item_endTime = models.TimeField(db_column='item_endTime', blank=True, null=True) 
	
	# def __init__(self, item_id, item_nickname, item_basePrice, item_isActive, item_startDate, item_endDate, item_startTime, item_endTime):
		# self.item_id = item_id
		# self.item_nickname = item_nickname
		# self.item_basePrice = item_basePrice
		# self.item_isActive = item_isActive
		# self.item_startDate = item_startDate
		# self.item_endTime = item_endDate
		# self.item_startTime = item_startTime
		# self.item_endTime = item_endTime

	def __str__(self):
		return str(self.item_id) + " " + self.menu_id.company_name + " " + self.item_nickname + " " + str(self.item_basePrice) + " " + str(self.item_startDate) + " " + str(self.item_endDate) + " " + str(self.item_startTime) + " " + str(self.item_endTime)

	#def __repr__(self):
	#	return '<Menu %r, %r, %r>' %(self.item_id, self.item_nickname, self.item_basePrice)
	
	def realPrice(self):
	# make sure it returns a real number
		return self.item_basePrice/ 100.0
	
	class Meta:
		managed = False
		db_table = 'Menu'
		
		
class Size(models.Model):
    size_id = models.AutoField(primary_key=True)
    size_name = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
    	return str(self.size_id) + " " + self.size_name

    class Meta:
        managed = False
        db_table = 'Size'
		
		
class Item(models.Model):
    id = models.AutoField(primary_key=True)  # AutoField?
    item_id =  models.ForeignKey(Menu, db_column='item_id', on_delete=models.CASCADE)
    category_id = models.ForeignKey(Category, db_column='category_id', on_delete=models.CASCADE)
    container_id = models.ForeignKey(Container, db_column='container_id', on_delete=models.CASCADE)
    options = models.CharField(max_length=1000, blank=True, null=True)
    options_isFixed = models.CharField(db_column='options_isFixed', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    options_price = models.CharField(max_length=1000, blank=True, null=True)
    item_mealOptions = models.CharField(db_column='item_mealOptions', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    item_mealPrice = models.CharField(db_column='item_mealPrice', max_length=1000, blank=True, null=True)  # Field name made lowercase.

    def __str__(self):
		return str(self.id) + " " + str(self.item_id.menu_id) + " " + str(self.container_id.container_id) + "," + self.options + "," + self.options_isFixed + "," + self.options_price + " " + self.item_mealOptions + " " + self.item_mealPrice

#   def __repr__(self):
		# return '<Item %r, %r, %r>' %(self.item_id, self.category_id, self.container_id)
    def itemSizes(self):

		itemSizesList = []
		actualSizesList = []
		sizesString = ""
		
		itemSizesList = ItemSize.objects.filter(item_id = self.item_id)
		
		for value in itemSizesList:
			actualSizesList.append(value.size_id.size_name)
			actualSizesList.append(value.itemSizePrice)
			
			if value.size_id.size_id == 6:
				actualSizesList.append(value.item_count)

		if actualSizesList:
			i = 0
			while i < len(actualSizesList):
				if actualSizesList[i] == 'Count':
					sizesString += "$" + str(int(actualSizesList[i+1])/100.00) 
					if i+3 == len(actualSizesList):
						if actualSizesList[i+2] == 1:
							sizesString += " per piece"
						else: 
							sizesString += " for " + str(actualSizesList[i+2]) + " pieces"
					else:
						if actualSizesList[i+2] == 1:
							sizesString += " per piece, "
						else: 
							sizesString += " for " + str(actualSizesList[i+2]) + " pieces, "
					i += 3
				else:
					sizesString += str(actualSizesList[i]) + " "
					
					if i+2 == len(actualSizesList):
						sizesString += " (+ $" + str(int(actualSizesList[i+1])/100.00) + ")"
					else:
						sizesString += " (+ $" + str(int(actualSizesList[i+1])/100.00) + "), "
					i += 2
			return sizesString
		return "No Specified Size"

    def mainItems(self):

		fixedOptionsindexes= []
		fixedOptions = []
		fixedString = ""

		fixedList = self.options_isFixed.split(',')
		optionsList = self.options.split(',')
		
		for index, value in enumerate(fixedList):
			if value == "main":
				fixedOptionsindexes.append(optionsList[index])
		
		for i in fixedOptionsindexes:
			fixedOptions.append(str((Option.objects.get(option_id = i)).option_name))
		
		if fixedOptions:
			for i, val in enumerate(fixedOptions):
				if i+1 == len(fixedOptions):
					fixedString += val
				else:
					fixedString += val
					fixedString += ", "			
			return fixedString
		
		return "No Main Ingredients"
		
    def fixedItems(self):

		fixedOptionsindexes= []
		fixedOptions = []
		fixedString = ""

		fixedList = self.options_isFixed.split(',')
		optionsList = self.options.split(',')
		
		for index, value in enumerate(fixedList):
			if value == "fixed":
				fixedOptionsindexes.append(optionsList[index])
		
		for i in fixedOptionsindexes:
			fixedOptions.append(str((Option.objects.get(option_id = i)).option_name))
		
		if fixedOptions:
			for i, val in enumerate(fixedOptions):
				if i+1 == len(fixedOptions):
					fixedString += val
				else:
					fixedString += val
					fixedString += ", "			
			return fixedString
		
		return "No Fixed Ingredients"
		
    def optionalItems(self):
		
		fixedOptionsindexes= []
		optionsPriceindexes = []
		fixedOptions = []
		fixedString = ""
		
		fixedList = self.options_isFixed.split(',')
		optionsList = self.options.split(',')
		optionsPriceList = self.options_price.split(',')

		for index, value in enumerate(fixedList):
			if value == "optional":
				fixedOptionsindexes.append(optionsList[index])
				optionsPriceindexes.append(optionsPriceList[index])

		for i, value in enumerate(fixedOptionsindexes):
			fixedOptions.append(str((Option.objects.get(option_id = value)).option_name))
			fixedOptions.append(str(optionsPriceindexes[i]))
			
		if fixedOptions:
			for i, val in enumerate(fixedOptions):
				if i+1 == len(fixedOptions):
					fixedString += " (+ $" + str(int(val)/100.00) + ")"

				else:
					if i%2 == 1:
						fixedString += "(+ $" + str(int(val)/100.00) + "), "
					else:
						fixedString += val
			return fixedString
		
		return "No Optional Ingredients"

		
    def mealOptions(self):	
		mealOption = []
		finalmealList = []
		mealString = ""
		
		mealList = self.item_mealOptions.split(',')
		mealPriceList = self.item_mealPrice.split(',')

		for index, value in enumerate(mealList):
			
			mealOption = value.split('-')
			
			finalmealList.append(str((Size.objects.get(size_id = mealOption[1])).size_name))
			finalmealList.append(str((Option.objects.get(option_id = mealOption[0])).option_name))
			finalmealList.append(str(mealPriceList[index]))

		if finalmealList:
			for i, value in enumerate(finalmealList):
				if i%3 == 2:
					if i+1 == len(finalmealList):
						mealString += " (+ $" + str(int(value)/100.00) + ")"
					else:
						mealString += "(+ $" + str(int(value)/100.00) + "), "
				else:
					mealString += value + " "
			return mealString
		
		return "No Meal Options"
	
    class Meta:
        managed = False
        db_table = 'Item'

class ItemSize(models.Model):
	id = models.AutoField(primary_key=True)  
	item_id =  models.ForeignKey(Menu, db_column='item_id', on_delete=models.CASCADE)
	size_id = models.ForeignKey(Size, db_column='size_id', on_delete=models.CASCADE)
	itemSizePrice = models.IntegerField(db_column='itemSizePrice')
	item_count = models.IntegerField(db_column='item_count')

	def __str__(self):
		return str(self.id) + " " + str(self.item_id.item_id) + " " + str(self.size_id.size_id) + " " + str(self.itemSizePrice) + " " + str(self.item_count)

	class Meta:
		managed = False
		db_table = 'Item-Size'

class AuthGroup(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()
    username = models.CharField(unique=True, max_length=30)

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    action_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'
