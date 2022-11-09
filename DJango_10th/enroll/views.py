from django.shortcuts import render
from .forms import StuRegForm
from django.http import HttpResponseRedirect
# Create your views here.

def thankyou(request):
    return render(request,'enroll/newRegister.html') 

def showData(request):
    if request.method == 'POST':
        fm = StuRegForm(request.POST)
        if  fm.is_valid():
            print('---------------------------------------------------------------------------------------')
            Name = fm.cleaned_data['name']
            Email = fm.cleaned_data['email']
            print('Name : ',Name)
            print('Email: ',Email)
            return HttpResponseRedirect('/out/successful/')
            # return render(request,'enroll/newRegister.html')
    else :
        fm = StuRegForm()
        
    return render(request,'enroll/stuRegister.html',{'form':fm})


