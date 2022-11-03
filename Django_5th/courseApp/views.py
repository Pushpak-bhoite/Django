from django.shortcuts import render

# Create your views here.
myCon ={'name':'siya_ram'}
def course_F1(request):
    return render(request,'course/courseOne.html', context = myCon)