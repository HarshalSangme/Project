from asyncio.windows_events import NULL
from wsgiref.util import request_uri
from django.db import models
from datetime import datetime
from datetime import date
from django.utils.translation import gettext as _
# Create your models here.

class EmployeesRequest(models.Model):
    request_id = models.IntegerField()
    author = models.IntegerField()
    status = models.CharField(max_length=191, null=False, blank=False)
    resolved_by = models.IntegerField()
    request_created_at = models.DateField()
    vaccation_start_date = models.DateField()
    vaccation_end_date = models.DateField()

    # vaccation_start_date = models.DateField(_("Date"), default=date.today)
    # vaccation_end_date = models.DateField(_("Date"), default=date.today)

    def __str__(self):
        return self.author

# Creating Custom model for creating table in database

class EmployeeDetailsTable(models.Model):

    employee_id = models.IntegerField()
    employee_name  = models.CharField(max_length=50, null = False, blank = False)
    holiday_taken  = models.IntegerField()
    employee_email_id = models.CharField(max_length=50, null = False, blank = False)
    employee_password = models.CharField(max_length=50, null = False, blank = False)

    def __str__(self):
        return self.employee_name