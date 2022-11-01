from django.urls import path
from . import views 

urlpatterns = [
    path('feesF1/',views.fee_fun1),
    path('feesF2/',views.fee_fun2)
]