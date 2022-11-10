from django.contrib import admin
from .models import StuData

# Register your models here.
@admin.register(StuData)
class UserAmin(admin.ModelAdmin):
    list_display = ('id', 'name' ,'email','password')

