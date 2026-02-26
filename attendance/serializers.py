from rest_framework import serializers
from .models import Attendance
from employees.models import Employee
from datetime import date

class AttendanceSerializer(serializers.ModelSerializer):
    employee_id = serializers.SlugRelatedField(queryset=Employee.objects.all(), source='employee', slug_field='employee_id')
    employee_name = serializers.CharField(source='employee.full_name', read_only=True)
    employee_code = serializers.CharField(source='employee.employee_id', read_only=True)

    class Meta:
        model = Attendance
        fields = ['id', 'employee_id', 'employee_name', 'employee_code', 'date', 'status', 'marked_at']
        read_only_fields = ['id', 'marked_at', 'employee_name', 'employee_code']

    def validate_date(self, value):
        if value > date.today():
            raise serializers.ValidationError("Attendance date cannot be in the future.")
        return value
    
    def validate(self, data):
        employee = data.get('employee')
        date_value = data.get('date')
        if Attendance.objects.filter(employee=employee, date=date_value).exists():
            raise serializers.ValidationError(f"Attendance for this employee on {date_value} is already marked.")
        return data