from statistics import mode
from django.db import models

# Create your models here.

class Userinfo(models.Model):
    name=models.CharField(max_length=30)
    gender=models.CharField(max_length=10)



    class Meta:
        db_table="User_master2"

    def __str__(self):
        return f'''{self.__dict__}'''

    def __repr__(self):
        return str(self)

    