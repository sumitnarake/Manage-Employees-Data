from django.contrib import admin
from employee.models import employeenames
# Register your models here.

class rgempnames(admin.ModelAdmin):
    list_display=['name','email','address','phone']

admin.site.register(employeenames,rgempnames)