from django import forms
from django.contrib.auth.forms import PasswordChangeForm, AuthenticationForm, UsernameField,PasswordResetForm, SetPasswordForm
from django.contrib.auth.models import User
from django.contrib.auth import password_validation



class MyPasswordChangeForm(PasswordChangeForm):
	old_password = forms.CharField(label=("Old Password"),
		strip=False, widget=forms.PasswordInput(attrs={'autocomplete':'current-password', 'autofocus':True,
			'class':'form-control'}))


	new_password1 = forms.CharField(label=("New Password"),
		strip=False, widget=forms.PasswordInput(attrs={'autocomplete':'new-password', 'autofocus':True,
			'class':'form-control'}),help_text=password_validation.password_validators_help_text_html())	


	new_password2 = forms.CharField(label=("Confirm New Password"),
		strip=False, widget=forms.PasswordInput(attrs={'autocomplete':'new-password', 'autofocus':True,
			'class':'form-control'}))	

class MyPasswordResetForm(PasswordResetForm):
		email = forms.EmailField(label=("Email"),max_length=254,
			widget=forms.EmailInput(attrs={'autocomplete':'email', 'autofocus':True,
			'class':'form-control'}))

class MySetPasswordForm(SetPasswordForm):
	new_password1 = forms.CharField(label=("New Password"),
		strip=False, widget=forms.PasswordInput(attrs={'autocomplete':'new-password', 'autofocus':True,
			'class':'form-control'}),help_text=password_validation.password_validators_help_text_html())	


	new_password2 = forms.CharField(label=("Confirm New Password"),
		strip=False, widget=forms.PasswordInput(attrs={'autocomplete':'new-password', 'autofocus':True,
			'class':'form-control'}))	