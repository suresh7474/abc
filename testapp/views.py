from django.shortcuts import render
from rest_framework.generics import ListAPIView,CreateAPIView,DestroyAPIView,RetrieveDestroyAPIView
from testapp.models import Employee
from testapp.serializer import EmployeeSerilizer
from rest_framework.viewsets import ModelViewSet
class EmployeeAPIView(ListAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerilizer

class EmployeeCreateAPIView(CreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerilizer

class EmployyeRetrievDestoyAPIView(RetrieveDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerilizer
    lookup_field = 'id'

class Employee_detail(ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerilizer