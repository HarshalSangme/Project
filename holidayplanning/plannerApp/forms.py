from pyexpat import model
from attr import field, fields
from django import forms
from .models import EmployeesRequest

class updateRequestForm(forms.ModelForm):
    class Meta:
         model = EmployeesRequest
         fields = ['request_id', 'author', 'status', 'resolved_by']

    # request_id = forms.IntegerField()
    # author = forms.IntegerField()
    # status = forms.CharField()
    
