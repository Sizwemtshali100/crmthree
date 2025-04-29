from django import forms
from django.forms import ModelForm
from . models import CustomerModel
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
        
class CustomerForm(ModelForm):
    class Meta:
        model = CustomerModel
        fields = ['Region','Rep','Items','Units','Cost']

        widgets = {           
            'Region':forms.Select(attrs={'class':'form-control'}),
            'Rep':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter a name'}),
            'Items' : forms.Select(attrs={'class':'form-control'}),
            'Units': forms.TextInput(attrs={'class':'form-control','placeholder':'Enter the Integer value'}),
            'Cost' : forms.TextInput(attrs={'class':'form-control','placeholder':'Enter a Decimal value'}),
        }

class CustomerRegistration(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

        widgets = {           
            #'Region':forms.Select(attrs={'class':'form-control'}),
            #'Items' : forms.Select(attrs={'class':'form-control'}),
            'username':forms.TextInput(attrs={'class':'form-control'}),
            'password1': forms.TextInput(attrs={'class':'form-control'}),
            'password2': forms.TextInput(attrs={'class':'form-control'}),
        }

