from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from .models import *
from .models import order

class CustomerForm(ModelForm):
	class Meta:
		model = Customer
		fields = '__all__'
		exclude = ['user','membership','price','subject','message']
class Customer1Form(ModelForm):
	class Meta:
		model = Customer
		fields = '__all__'
		exclude = ['user','profile_pic']
class OrderForm(ModelForm):
	class Meta:
		model = order
		fields = '__all__'

class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']

class ContactForm(forms.Form):
	full_name = forms.CharField(max_length = 50)
	phone = forms.CharField(max_length = 50)
	email_address = forms.EmailField(max_length = 150)
	subject=forms.CharField(max_length=50)
	message = forms.CharField(widget = forms.Textarea, max_length = 2000)
class QuestionForm(forms.ModelForm):
    class Meta:
        model=Question
        fields=['description']
        widgets = {
        'description': forms.Textarea(attrs={'rows': 6, 'cols': 30})
        }
class QuestionForm1(forms.ModelForm):
    class Meta:
        model=Idea
        fields=['description']
        widgets = {
        'description': forms.Textarea(attrs={'rows': 25, 'cols': 50})
        }
class CustomerUserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','password']
        widgets = {
        'password': forms.PasswordInput()
        }
class CustomerForm(forms.ModelForm):
    class Meta:
        model=Customer
        fields='__all__'
        exclude = ['user','membership','price']


