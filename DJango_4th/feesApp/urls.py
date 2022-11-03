

# from django.urls import URLPattern


from django.urls import path
from . import views


urlpatterns = [
    path('fees_F1/',views.fees_F1),
    path('fees_F2/',views.fees_F2)
]
