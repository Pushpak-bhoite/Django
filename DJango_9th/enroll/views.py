from django.shortcuts import render
from .forms import StuRegister
# Create your views here.
def showData(request):
    if request.method == 'POST' :
        fm = StuRegister(request.POST)  #this is anather form creted with their values
        print(fm)
        print(" This above Form is with with their keys & values ")
    else:
        fm = StuRegister() 
        print('GET method is called ')
    return render(request,'enroll/userRegister.html',{'form':fm})  #This is empty form
    
