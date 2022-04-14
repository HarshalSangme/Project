from rest_framework import serializers

from .models import EmployeesRequest

class EmployeesRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeesRequest
        fields = '__all__'


from .models import EmployeeDetailsTable

# class EmployeesRegistrationSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = EmployeeDetailsTable
#         fields = '__all__'

#  ---------------------- Creating New Employee ---------------------

class CreateNewEmployeeSerializer(serializers.ModelSerializer):
     class Meta:
         model = EmployeeDetailsTable
         fields = ('employee_id','employee_name', 'holiday_taken', 'employee_email_id','employee_password')
    
     def validate(self, attrs):
         if EmployeeDetailsTable.objects.filter(employee_email_id = attrs['employee_email_id']).exists():
             raise serializers.ValidationError({'employee_email_id', ('Employees Email id already exists')})

         return super().validate(attrs)
    
    #  def create(self, validated_data):
    #      return EmployeeDetailsTable.objects.create_user(validated_data)
    