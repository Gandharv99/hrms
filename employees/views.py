from rest_framework.generics import ListCreateAPIView, DestroyAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import NotFound
from .models import Employee
from .serializers import EmployeeSerializer

# Create your views here.
class EmployeeListCreateView(ListCreateAPIView):
    """
    GET /api/employees/ - List all employees
    POST /api/employees/ - Create a new employee
    """
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class EmployeeDeleteView(DestroyAPIView):
    """
    DELETE /api/employees/{employee_id}/ - Delete an employee by EMPLOYEE ID
    """
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    def get_object(self):
        employee_id = self.kwargs.get('employee_id')
        try:
            return Employee.objects.get(employee_id=employee_id)
        except Employee.DoesNotExist:
            raise NotFound(f"Employee with ID {employee_id} does not exist.")

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        employee_id = instance.employee_id
        self.perform_destroy(instance)
        return Response(
            {"message": f"Employee with ID {employee_id} has been deleted."},
            status=status.HTTP_200_OK
        )