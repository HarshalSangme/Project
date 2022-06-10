from django.urls import path
from . import views

#  JWT Token Authentication 
# from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView


urlpatterns = [

    path('', views.index, name='index'),

# /////////////////////////////////// EMPLOYEE SIDE PATH ////////////////////////////////
# ..................................................................................

    
    path('employees/', views.employees, name='employeesName'),
    path('employeesRegistrationPages/', views.employeesRegistration, name='employeesRegistration'),
    path('employeesLoginPages/', views.employeesLogin, name='employeesLogin'),

# .................................. Employee API.................................
    # Employee Creating Request
    path('employeeCreatingRequest',views.CreateHolidayRequestApi, name='employeeCreatingRequest'),

    # Employee Registration Api
    path('employeeRegistrationApi', views.EmployeeRegistrationWithApi, name='employeeRegistrationRequestApi'),
    # Employee Registration With User Interface
    path('employeeRegistrationUserInterface/', views.EmployeeRegistrationWithUserInterface,  name='employeeRegistrationUserInterface'),


# /////////////////////////////////// MANAGER SIDE PATH ////////////////////////////////
# ..................................................................................

    path('managers/', views.managers, name='managersName'),
    path('managersRegistrationPages/', views.managersRegistration, name='managersRegistration'),
    path('managersLoginPages/', views.managersLogin, name='managersLogin'),

# .................................. MANAGER API.................................
    
    path('managersPageRequest/', views.ShowAllRequestApi, name='managersPageRequest'),
    path('RequestPage/', views.DisplayAllRequestUI, name='mangerRequestpageUI'),



# *********************************** Update Reqeusts **********************************
    path('updateRequests/', views.updateRequestsAll, name='updateRequestsName'),
    path('updateRequests/results', views.updateRequestSearch, name='urlUpdateRequestSearch'),  # with the help of Seacrh Field

    path('updateRequestsForm/<int:id>', views.updateRequestWithId, name='urlUpdateRequestId'), # with the help of Id which is inside For Loop
    
    path('updateRequestsCURD/<int:id>', views.updateRequestCURD, name='urlUpdateRequestCURD'),

    # path('updateRequests/save', views.updateRequestsForms, name='urlUpdateRequestForms'),

# *********************************** Delete Requests ***************************************
   path('DeleteRequests/<int:id>', views.deleteRequest, name='urldeleteRequest' )  # with the help of Id which is inside For Loop

    
]
