from django.shortcuts import render
# from django.http import path


# Create your views here.
def fees_F1 (request):
    return render(request,'fees/feesOne.html')

def fees_F2(request) :
    return render(request,'fees/feesTwo.html')