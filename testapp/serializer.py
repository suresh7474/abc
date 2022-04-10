from rest_framework.serializers import ModelSerializer
from testapp.models import Employee



class EmployeeSerilizer(ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'
