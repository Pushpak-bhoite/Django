from django import forms

class StuRegForm (forms.Form) :
    name = forms.CharField()
    email =forms.EmailField()
    # passward = forms.PasswordInput()

