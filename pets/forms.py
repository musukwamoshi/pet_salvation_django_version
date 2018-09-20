from django import forms
from django.conf import settings

#form for pets
class PetForm(forms.Form):

	PROVINCE_OPTIONS = settings.PROVINCE_OPTIONS

	TOWN_OPTIONS = settings.TOWN_OPTIONS


	petname=forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Pet Name'}),required=True,max_length=20)
	poster=forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Posted by'}),required=True,max_length=100)
	email=forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Email'}),required=True,max_length=100)
	area=forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Area'}),required=True,max_length=100)
	town = forms.ChoiceField(choices=TOWN_OPTIONS, widget=forms.Select(attrs={'class':'form-control'}))
	province = forms.ChoiceField(choices=PROVINCE_OPTIONS, widget=forms.Select(attrs={'class':'form-control'}))
	contact=forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Contact Number'}),required=True,max_length=12)
	description=forms.CharField(required=True,widget=forms.Textarea(attrs={'class': 'form-control','placeholder':'Description'}))
	file=forms.FileField()


#form for contact
class ContactForm(forms.Form):

	PROVINCE_OPTIONS = settings.PROVINCE_OPTIONS
	TOWN_OPTIONS = settings.TOWN_OPTIONS

	
	name=forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Name'}),required=True,max_length=20)
	email=forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Email'}),required=True,max_length=100)
	area=forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Area'}),required=True,max_length=100)
	town = forms.ChoiceField(choices=TOWN_OPTIONS, widget=forms.Select(attrs={'class':'form-control'}))
	province = forms.ChoiceField(choices=PROVINCE_OPTIONS, widget=forms.Select(attrs={'class':'form-control'}))
	contact=forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'ContactNumber'}),required=True,max_length=12)
	message=forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Message'}),required=True)




#form for contact
class LoginForm(forms.Form):


	username=forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Username'}),required=True,max_length=20)
	email=forms.CharField(widget=forms.EmailInput(attrs={'class': 'form-control','placeholder':'Email'}),required=True,max_length=100)
	password=forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control','placeholder':'Password'}),required=True,max_length=100)
	
	
