from django.urls import  path

from . import views

urlpatterns = [
    path('out/',views.showData)
]