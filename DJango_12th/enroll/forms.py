from django import forms
from django.core import validators
from .models import StuData

class StuRegForm(forms.ModelForm):
    class Meta:
        model = StuData
        fields = ['name','email','password']
        widgets = {'password':forms.PasswordInput,
                   'name':forms.TextInput(attrs={'class':'myclass','placeholder':'Enter Your Name'})}

        labels = {'name':'Enter Name','email':'Enter Email' ,'password':'Enter Password'}
        error_messages = {
            'name':{'required':'Jueli Please Enter your name '},
            'email':{'required':'Jueli Please Enter your Eamil '}
            }
        


# class StuRegForm(forms.Form):
    # name = forms.CharField()
    # email = forms.EmailField()
    # password = forms.CharField(widget=forms.PasswordInput)