from rest_framework.generics import ListCreateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Q, Count
from django.utils import timezone
from .models import Attendance
from .serializers import AttendanceSerializer
from employees.models import Employee

# Create your views here.
class AttendanceListCreateView(ListCreateAPIView):
    serializer_class = AttendanceSerializer

    def get_queryset(self):
        querset = Attendance.objects.select_related('employee').all()
        employee_id = self.request.query_params.get('employee_id')
        date = self.request.query_params.get('date')

        if employee_id:
            querset = querset.filter(employee_id=employee_id)
        if date:
            querset = querset.filter(date=date)
        return querset
    
class AttendanceSummaryView(APIView):
    def get(self, request):
        today = timezone.localdate()
        total_employees = Employee.objects.count()

        today_present = Attendance.objects.filter(date=today, status='Present').count()
        today_absent = Attendance.objects.filter(date=today, status='Absent').count()

        employee_summary = Employee.objects.annotate(total_present=Count('attendance_records', filter=Q(attendance_records__status='Present')),
                                                     total_absent=Count('attendance_records', filter=Q(attendance_records__status='Absent'))).values('id', 'employee_id', 'full_name', 'total_present', 'total_absent')
        return Response({
            'total_employees': total_employees,
            'today': str(today),
            'today_present': today_present,
            'today_absent': today_absent,
            'employee_summary': list(employee_summary)
        }, status=status.HTTP_200_OK)