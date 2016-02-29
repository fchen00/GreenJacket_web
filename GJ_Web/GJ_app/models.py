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
	
	def __repr__(self):
		return '<User %r, %r, %r>' % self.name, self.company_name, self.is_admin

class Branch(models.Model):
    branch_id = models.AutoField(primary_key=True)
    company_id = models.ForeignKey(User, db_column='company_id', on_delete=models.CASCADE)
    branch_phone = models.CharField(max_length=12, blank=True, null=True)
    branch_address = models.CharField(max_length=200, blank=True, null=True)
    branch_city = models.CharField(max_length=200, blank=True, null=True)
    branch_state = models.TextField(blank=True, null=True)  # This field type is a guess.
    branch_zipcode = models.TextField(blank=True, null=True)  # This field type is a guess.
    date_added = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Branch'


class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Category'

class Option(models.Model):
    option_id = models.AutoField(primary_key=True)
    option_name = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Option'

class CategoryOption(models.Model):
    id = models.AutoField(primary_key=True)  
    category_id = models.ForeignKey(Category, db_column='category_id', on_delete=models.CASCADE)
    option_id = models.ForeignKey(Option, db_column='option_id', on_delete=models.CASCADE)

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
    credit_number = models.TextField(blank=True, null=True)  # This field type is a guess.
    credit_expiration = models.TextField(blank=True, null=True)  # This field type is a guess.
    credit_cvv = models.CharField(max_length=4, blank=True, null=True)
    credit_zipcode = models.TextField(blank=True, null=True)  # This field type is a guess.
    date_created = models.DateField(blank=True, null=True)
    last_updated = models.DateField(blank=True, null=True)
    is_active = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'Company'


class Container(models.Model):
    container_id = models.AutoField(primary_key=True)
    container_name = models.CharField(max_length=200, blank=True, null=True)

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
    item_startTime = models.TimeField(db_column='item_startTime', blank=True, null=True)  # Field name made lowercase.
    item_endTime = models.TimeField(db_column='item_endTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Menu'
		
	def __init__(self, user_id, company_name, email, password, qr_code, is_admin):
		self.item_id = item_id
		self.menu_id = menu_id
		self.item_nickname = item_nickname
		self.item_basePrice = item_basePrice
		self.item_isActive = item_isActive
		self.item_startDate = item_startDate
		self.item_endTime = item_endDate
		self.item_startTime = item_startTime
		self.item_endTime = item_endTime
	
	def __repr__(self):
		return '<Menu %r, %r, %r>' % self.item_id, self.item_nickname, self.item_basePrice


class Size(models.Model):
    size_id = models.AutoField(primary_key=True)
    size_name = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Size'
		
		
class Item(models.Model):
    id = models.AutoField(primary_key=True)  # AutoField?
    item_id =  models.ForeignKey(Menu, db_column='item_id', on_delete=models.CASCADE)
    category_id = models.ForeignKey(Category, db_column='category_id', on_delete=models.CASCADE)
    container_id = models.ForeignKey(Container, db_column='container_id', on_delete=models.CASCADE)
    size_id = models.ForeignKey(Size, db_column='size_id', on_delete=models.CASCADE)
    options = models.CharField(max_length=1000, blank=True, null=True)
    options_isFixed = models.CharField(db_column='options_isFixed', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    options_price = models.CharField(max_length=1000, blank=True, null=True)
    item_mealOptions = models.CharField(db_column='item_mealOptions', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    item_mealPrice = models.CharField(db_column='item_mealPrice', max_length=1000, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Item'


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
