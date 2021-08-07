from django.contrib import admin
from .models import Mydb
# Register your models here.

admin.site.register(Mydb)

class Myadmin(admin.ModelAdmin):
    fields= ['age']