from django.shortcuts import render
from .forms import StuRegForm
# Create your views here.

def showData(request):
    if request.method == 'POST':
        fm = StuRegForm(request.POST)
        if  fm.is_valid():
            print('---------------------------------------------------------------------------------------')
            Name = fm.cleaned_data['name']
            Email = fm.cleaned_data['email']
            print('Name : ',Name)
            print('Email: ',Email)

            return render(request,'enroll/newRegister.html')
    else :
        fm = StuRegForm()
        
    return render(request,'enroll/stuRegister.html',{'form':fm})


