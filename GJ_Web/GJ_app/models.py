from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
import datetime 

# Create your models here.

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def was_published_recently(self):
    	return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    def __str__ (self):
    	return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__ (self):
    	return "Question " + self.question.question_text + " Chioce " + self.choice_text


class Company(models.Model):
    username = models.CharField(max_length=200, blank= False, null=False)
    password = models.CharField(max_length=200, blank= False, null=False)
    email = models.CharField(max_length=200, blank= False, null=False)
    security_question = models.CharField(max_length=1000, blank= False, null=False)
    comp_name = models.CharField(max_length=200, blank= False, null=False)
    num_store = models.IntegerField(blank= False, null=False)
    address = models.CharField(max_length=200, blank= False, null=False)
    creditnum = models.CharField(max_length=200, blank= False, null=False)

    def __str__(self):
        return self.username + " " + str(self.num_store)


#Create an instance of Company in the database 
# 1. python manage.py makemigrations
# 2. python manage.py migrate
# 3. python mangae.py shell
# 4. from GJ_app.models import *
# 5. Company.objects().all()  checking if there is any instance in Company
# 6. k=Company(username="aaaa", password="aaaa", email="aaa@aaa.com", security_question="Who am I?", comp_name="aaaacomp", num_store=1, address="garbage", creditnum= "123456786954")
# 7. k.save()  FInally saving it

# k=Company(username="aaaa", password="aaaa", email="aaa@aaa.com", security_question="Who am I?", comp_name="aaaacomp", num_store=1, address="garbage", creditnum= "123456786954")
# k=Company(username="bbbb", password="bbbb", email="bbb@bbb.com", security_question="Who are you?", comp_name="bbbbcomp", num_store=2, address="happybirth", creditnum= "12312412312")
# k=Company(username="cccc", password="cccc", email="cccc@cccc.com", security_question="Who who who?", comp_name="cccccomp", num_store=4, address="wowowow", creditnum= "124321786954")
# k=Company(username="dddd", password="dddd", email="dddd@dddd.com", security_question="Whats my name?", comp_name="ddddcomp", num_store=4, address="hahahaha", creditnum= "283321786954")
# k=Company(username="eeee", password="eeee", email="eeee@eeee.com", security_question="How are you?", comp_name="eeeecomp", num_store=6, address="yeyeyeye", creditnum= "283321786954")
# k=Company(username="ffff", password="ffff", email="ffff@ffff.com", security_question="Where do I live?", comp_name="ffffcomp", num_store=8, address="muhahaha", creditnum= "283324692954")
# k=Company(username="gggg", password="gggg", email="gggg@gggg.com", security_question="What are you doing?", comp_name="ggggcomp", num_store=4, address="papapapa", creditnum= "253124692954")
# k=Company(username="hhhh", password="hhhh", email="hhhh@hhhh.com", security_question="What are your name?", comp_name="hhhhcomp", num_store=3, address="bababab", creditnum= "253124692954")
# k=Company(username="IIII", password="IIII", email="IIII@IIII.com", security_question="Who is your teacher?", comp_name="IIIIcomp", num_store=1, address="waawawa", creditnum= "253124697454")
# k=Company(username="JJJJ", password="JJJJ", email="JJJJ@JJJJ.com", security_question="Who's your daddy?", comp_name="JJJJcomp", num_store=3, address="jajajjaja", creditnum= "253432197454")
# k=Company(username="KKKK", password="KKKK", email="KKKK@KKKK.com", security_question="Daddy is who?", comp_name="KKKKcomp", num_store=5, address="KKKKKKa", creditnum= "253634297454")




