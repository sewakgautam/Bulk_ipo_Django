from email.policy import default
from click import password_option
from django import forms

class Logins(forms.Form):
    Username = forms.CharField(label='Username')
    Password = forms.CharField(label='Password')

class Dmat(forms.Form):
    Name = forms.CharField(label='Name')
    Boid = forms.IntegerField(label='Boid')
    Crn = forms.CharField(label='Crn')
    Apply = forms.IntegerField(label='kitta')
    Pin = forms.IntegerField(label='pin')
