from django.shortcuts import render

# Create your views here.
def course_fun1(request):
    return render(request,'courseOne.html')

def course_fun2(request) :
    return render(request,'courseTwo.html')