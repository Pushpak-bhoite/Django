from django.shortcuts import render

# Create your views here.
def fee_fun1(request):
    return render(request,'feesOne.html')

def fee_fun2(request):
    return render (request,'feesTwo.html')