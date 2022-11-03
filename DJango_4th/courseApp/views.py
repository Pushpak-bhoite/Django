from django.shortcuts import render

# Create your views here.
def course_F1(request) :
    return render (request ,'course/courseOne.html')

def course_F2(request) :
    return render (request ,'course/coursetwo.html')