from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import UserProfile

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email' ,'password1', 'password2']

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']

class UserProfileForm(forms.ModelForm):
	class Meta:
		model = UserProfile
		fields = ['first_name','middle_name','last_name','identification_no', 'birthday','secret_question']

class ProfileUpdateForm(forms.ModelForm):
	class Meta:
		model = UserProfile
		fields = ['first_name','middle_name', 'last_name','identification_no','birthday','secret_question']
