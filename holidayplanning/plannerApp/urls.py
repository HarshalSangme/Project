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
    path('employeeRegistrationApi', views.CreateEmployeeApi, name='employeeRegistrationRequestApi'),
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


# JWT Token Auth UrL

    # path('gettoken/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('refreshtoken/', TokenRefreshView.as_view(), name='token_refresh'),
    # path('verifytoken/', TokenVerifyView.as_view(), name='token_verify')


]