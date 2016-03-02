from django import forms
from models import *

class RegistrationForm(forms.ModelForm):

	class Meta: #defind anything that is not realated to the class field
		model = User
		
