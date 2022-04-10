from django.contrib import admin
from testapp.models import Employee

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['id','ename','esal','eaddr']
    ordering = ['id']

admin.site.register(Employee,EmployeeAdmin)
