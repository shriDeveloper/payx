from .models import Group
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class GroupForm(ModelForm):
	class Meta:
		model = Group
		fields = ('name','description')

	def __init__(self, *args, **kwargs):
		super(GroupForm, self).__init__(*args, **kwargs)
        # for example change class for integerPolje1
		self.fields['name'].widget.attrs['class'] = 'mb-3'
		self.fields['description'].widget.attrs['class'] = 'mb-3'
		


class UserRegistrationForm(UserCreationForm):
	email = forms.EmailField(required = True)

	class Meta:
		model = User
		fields = ("username","email","password1","password2")

	def save(self,commit = True):
		user = super (UserRegistrationForm , self).save(commit = False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user