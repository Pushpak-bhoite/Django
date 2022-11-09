from django.shortcuts import render
from .forms import StuRegister
# Create your views here.
def showData(request):
    if request.method == 'POST' :
        fm = StuRegister(request.POST)  #this is anather form creted with their values
# Now see data accessing ways
        if fm.is_valid() :              #Check data is valid or not
            print("Claned DATA",fm.cleaned_data)
            print("___________________________________________________________")

            print("Name : ",fm.cleaned_data['name'])
            print("Email : ",fm.cleaned_data['email'])
            print("___________________________________________________________")

            name = fm.cleaned_data['name']
            email = fm.cleaned_data['email']
            print("Name : ",name)
            print("Email : ",email)
           
        
    else:
        fm = StuRegister() 
        print('GET method is called ')
    return render(request,'enroll/userRegister.html',{'form':fm})  #This is empty form
    
