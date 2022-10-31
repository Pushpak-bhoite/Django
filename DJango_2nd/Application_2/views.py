from django.shortcuts import render
from django.http import  HttpResponse
# Create your views here.

def s_A_f_fun(request):
    return HttpResponse("I'm in 2nd Application in 1st function")

def s_A_s_fun(request):
    return HttpResponse("I'm in 2nd Application in 2nd Function")