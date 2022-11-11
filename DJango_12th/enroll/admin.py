from django.contrib import admin
from .models import StuData
# Register your models here.

@admin.register(StuData)
class MyClass(admin.ModelAdmin):
    list_display = ('id','name','email','password')


