from statistics import mode
from django.db import models

# Create your models here.

class Userinfo(models.Model):
    fname=models.CharField(max_length=30)
    lname=models.CharField(max_length=30)
    email=models.EmailField(unique=True)    
    gender=models.CharField(max_length=12)    

    #gender=models.CharField(max_length=10)



    class Meta:
        db_table="Userinfo"

    def __str__(self):
        return f'''{self.__dict__}'''

    def __repr__(self):
        return str(self)

    