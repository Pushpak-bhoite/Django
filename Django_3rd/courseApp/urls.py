from django.urls  import path
from . import views
urlpatterns = [
    path('courseF1/',views.course_fun1),
    path('courseF2/',views.course_fun2)
]