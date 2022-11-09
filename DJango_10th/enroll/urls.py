from django.urls import path
from . import views


urlpatterns = [
    path("in/",views.showData),
    path('successful/',views.thankyou)
]