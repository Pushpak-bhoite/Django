from django.urls import path
from Application_1 import views
urlpatterns = [
    path('a1_url/',views.f_A_f_fun),
    path('a2_url/',views.f_A_s_fun)
    ]
