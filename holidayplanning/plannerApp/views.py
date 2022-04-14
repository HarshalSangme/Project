from re import I
from unittest import result
from django.shortcuts import render
import requests
from .serializers import EmployeesRequestSerializer
from .serializers import CreateNewEmployeeSerializer
from .models import EmployeesRequest
from .models import EmployeeDetailsTable
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Importing Authentication 
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


# Create your views here.
def index(request):

    return render(request, 'userInterfacePages/index.html')


def employees(request):
    return render(request, 'employees/employees.html')

def employeesRegistration(request):
    return render(request, 'employees/loginRegistration/employees_registration.html')

def employeesLogin(request):
    return render(request, 'employees/loginRegistration/employees_login.html')

# .................................................................................

def managers(request):
    return render(request, 'managers/managers.html')

def managersRegistration(request):
    return render(request, 'managers/managerLoginRegistration/managers_registration.html')

def managersLogin(request):
    return render(request, 'managers/managerLoginRegistration/managers_login.html')


# /////////////////////////////////// Employee SIDE ////////////////////////////////
# ..................................................................................

# Creating Employee Registration Api 

# @api_view(['POST'])
# def EmployeeRegistrationApi(request):
#     serializer = EmployeesRegistrationSerializer(data=request.data)

#     if serializer.is_valid():
#         serializer.save()

#     print(serializer.errors)

#     return Response(serializer.data)

@api_view(['POST'])
def CreateEmployeeApi(request):
    # Pass JSON data from user POST request to serializer for validation
    create_serializer = CreateNewEmployeeSerializer(data=request.data)

    # Check if user POST data passes validation checks from serializer
    if create_serializer.is_valid():

      # If user data is valid, create a new todo item record in the database
      employeeRegistration_item_object = create_serializer.save()

      # Serialize the new todo item from a Python object to JSON format
      read_serializer = CreateNewEmployeeSerializer(employeeRegistration_item_object)

      # Return a HTTP response with the newly created todo item data
      return Response(read_serializer.data, status=201)

    # If the users POST data is not valid, return a 400 response with an error message
    return Response(create_serializer.errors, status=400)



# Employee Registration with the help of Api and rendering it into User Interface
def EmployeeRegistrationWithUserInterface(request):
    if request.method == 'POST':
        employee_id = request.POST.get('employee_id')
        employee_name = request.POST.get('employee_name')
        holiday_taken = request.POST.get('holiday_taken')
        employee_email_id = request.POST.get('employee_email_id')
        employee_password = request.POST.get('employee_password')

        # print(employee_id, employee_name, holiday_taken)

        data = {
            'employee_id' : employee_id,
            'employee_name': employee_name,
            'holiday_taken':holiday_taken,
            'employee_email_id':employee_email_id,
            'employee_password': employee_password
        }
        # print(employee_id, employee_name)

#         {
#             "employee_id": 222,
#             "employee_name": "Ravi",
#             "holiday_taken":20,
#             "employee_email_id": "harshalsangme15@gmail.com",
#             "employee_password":Harshal@333
#   }

        headers = {'Content-Type': 'application/json'}

        read = requests.post('http://127.0.0.1:8000/employeeRegistrationApi', json = data, headers = headers)
        
        return render(request, 'employees/loginRegistration/employee_registration_Api_UI.html')
    else:
        return render(request, 'employees/loginRegistration/employee_registration_Api_UI.html')


# Employee Login Api



# /////////////////////////////////// MANAGER SIDE ////////////////////////////////
# ..................................................................................

#  Employees Creating Request for Asking Holiday to Managers

@api_view(['POST'])
def CreateHolidayRequestApi(request):
    serializer = EmployeesRequestSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    print(serializer.errors)

    return Response(serializer.data)
  

# Employee creating request with the help of UserInterface 
def CreateHolidayRequestWithUserInterface(request):
    callHolidayRequestApi = requests.post('http://127.0.0.1:8000/employeeCreatingRequest')
    resultsi = callHolidayRequestApi.json()

    return render(request, 'employees/employeeCreatingRequest.html', {'EmployeesRequest':resultsi})








# /////////////////////////////////// MANAGER SIDE ////////////////////////////////
# ..................................................................................

@api_view(['GET'])
def ShowAllRequestApi(request):
    EmployeesRequestobject = EmployeesRequest.objects.all()
    serializer = EmployeesRequestSerializer(EmployeesRequestobject, many=True)
    return Response(serializer.data)

# Manager Viewing requests with the help of UserInterface 

def DisplayAllRequestUI(request):
    callApi = requests.get('http://127.0.0.1:8000/managersPageRequest/')
    results = callApi.json()

    return render(request, 'managers/managerRequestPage.html', {'EmployeesRequest':results})


# {
# "id":3,
# "request_id":903,
# "author":103,
# "status":"Requested",
# "resolved_by":1003,
# "request_created_at":"2022-04-08",
# "vaccation_start_date":"2022-04-08",
# "vaccation_end_date":"2022-04-08"
# }