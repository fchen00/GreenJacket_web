from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
import datetime 

# Create your models here.

class Menu(models.Model):
	
	item_id = models.AutoField(primary_key=True)
	company_id = models.ForeignKey(User, on_delete=models.CASCADE)
	item_nickname = models.CharField(max_length=200)
	item_basePrice = models.IntegerField()
	item_isActive = models.BooleanField(null=False)
	item_startDate = models.DateField(auto_now=False, auto_now_add=False)
	item_endDate = models.DateField(auto_now=False, auto_now_add=False)
	item_startTime = models.TimeField(auto_now=False, auto_now_add=False)
	item_endTime = models.TimeField(auto_now=False, auto_now_add=False)

	class Meta:
		db_table = 'Menu'
		
	def __init__(self, item_id, company_id, item_nickname, item_basePrice, item_isActive, item_startDate, item_endDate, item_startTime, item_endTime):
		self.item_id = item_id
		self.company_id = company_id
		self.item_nickname = item_nickname
		self.item_basePrice = item_basePrice
		self.item_isActive = item_isActive
		self.item_startDate = item_startDate
		self.item_endDate = item_endDate
		self.item_startTime = item_startTime
		self.item_endTime = item_endTime
	
	def showPrice(self):
		return self.item_basePrice/100

	def __str__ (self):
		return self.question_text

