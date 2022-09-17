from django.contrib import admin

# Register your models here.
from .models import Userinfo

admin.site.register(Userinfo) #THIS WILL ADD USERINFO SECTION TO DJANGO ADMIN PAGE