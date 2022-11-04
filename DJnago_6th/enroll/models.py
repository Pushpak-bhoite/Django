from django.db import models

# Create your models here.
class Student (models.Model):
    stuid=models.IntegerField()
    stuname=models.CharField(max_length=70)
    stuemail=models.EmailField(max_length=70)
    stupass=models.Field(max_length=70)
    # now we are adding new field so at the end always write some default value
    comment=models.CharField(max_length=40 , default='Not Available')

