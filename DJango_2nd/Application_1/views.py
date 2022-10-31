from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def f_A_f_fun(request) :
    return HttpResponse("I'm in 1st Application in first Function")

def f_A_s_fun(request) :
    return HttpResponse("Im in 1st Application in 2nd Function")
