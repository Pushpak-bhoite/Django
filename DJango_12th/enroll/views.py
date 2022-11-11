from django.shortcuts import render
from .forms import StuRegForm
from .models import StuData

# Create your views here.
def showData(request):
    if request.method == 'POST' :
        fm = StuRegForm(request.POST)
        if fm.is_valid() :

            dn = fm.cleaned_data['name']
            de = fm.cleaned_data['email']
            dp = fm.cleaned_data['password']

            obj = StuData(name=dn ,email=de ,password=dp)
            obj.save()

    else :
        fm = StuRegForm()

    return render(request,'enroll/stuRegister.html',{'form':fm})
