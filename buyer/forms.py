from django import forms
from .models import Address

class AddressForm(forms.ModelForm):
	class Meta:
		model = Address
		fields = ['add_line1','add_line2','area','pincode','city','state']
		widgets = {'add_line1':forms.TextInput(attrs={'class':'form-control'}),
		'add_line1':forms.TextInput(attrs={'class':'form-control'}),
		'add_line2':forms.TextInput(attrs={'class':'form-control'}),
		'area':forms.TextInput(attrs={'class':'form-control'}),
		'pincode':forms.NumberInput(attrs={'class':'form-control'}),
		'city':forms.TextInput(attrs={'class':'form-control'}),
		'state':forms.Select(attrs={'class':'form-control'}),

		}