from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from django.core.urlresolvers import reverse
from django.http import JsonResponse

from .models import *


def set_session(user):
    session["user"] = {
        "id": user.user_id,
        "email": user.email
    }

	
def is_logged_in():
    return session.has_key("user")
	

def is_admin(user):
	if user.is_admin:
		return True
	return False