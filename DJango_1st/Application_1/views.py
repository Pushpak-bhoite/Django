from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def MyFunction_1 (request):
    return HttpResponse("Jay Shreen Ram")

def MyFunction_2 (request):
    return HttpResponse('<h1> It is under h1 Tag </h1>')

def MyFunction_3 (request):
    return HttpResponse()

def MyFunction_3(request):
    a = 10 + 20
    return HttpResponse(a)

def MyFunction_4(request):
    a = " Yudhishira"
    return HttpResponse(f'This is anather one{a}')
