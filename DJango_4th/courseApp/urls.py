
from django.urls import path
from . import views

urlpatterns = [
    path('course_F1/',views.course_F1),
    path('course_F2/',views.course_F2)
]