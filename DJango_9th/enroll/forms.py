from django import forms
class StuRegister(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()