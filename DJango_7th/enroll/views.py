from django.shortcuts import render

from enroll.models import Student_1

# Create your views here.
def stuDetails(request):
    stud = Student_1.objects.all()
    return render (request,'enroll/stuDetails.html',{'stu':stud})