from django import forms
from .models import Hospital , Receiver
from django.contrib.auth.models import User
class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        fields = ('username','password','email')

class HospitalForm(forms.ModelForm):
	class Meta():
		model = Hospital
		fields = ('name','street','city','pin')


class ReceiverForm(forms.ModelForm):
	class Meta:
		model = Receiver
		fields = ('name','age','gender','street','city','pin','blood_group')


class BloodDetailForm(forms.ModelForm):
	class Meta:
		model = Hospital
		fields = ('blood_group',)