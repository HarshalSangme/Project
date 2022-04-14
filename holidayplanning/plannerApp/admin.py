from django.contrib import admin

from .models import EmployeesRequest
from .models import EmployeeDetailsTable
# Register your models here.

admin.site.register(EmployeesRequest)
admin.site.register( EmployeeDetailsTable)