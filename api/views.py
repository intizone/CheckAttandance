from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.decorators import api_view

from main.models import Staff, Attendance
from .serializers import StaffSerializer, AttendanceSerializer

from datetime import datetime

@api_view(['GET'])
def staff_list(request):
    staff = Staff.objects.all()
    serializer = StaffSerializer(staff, many=True)
    return Response(serializer.data)




@api_view(['POST'])
def staff_create(request, id):
    serializer = StaffSerializer(data=request.data)

    if serializer.is_valid():
        staff = Staff.objects.create(
                f_name = request.date.get('f_name'),
                l_name = request.data.get('l_name'),
                position = request.data.get('position'),
                email = request.data.get('email'),
        )
        staff.save()
        return Response(serializer.data)
    return Response(serializer.errors)


@api_view(['POST'])
def attendance_create(request):
    serializer = StaffSerializer(data=request.data)
    if serializer.is_valid():
        if request.data.get('came') == True:
            attendance = Attendance.objects.create(
                    staff = Staff.objects.get(id=id),
                    came = request.data.get(default=True),
                    came_time = datetime.now()
                    )
            attendance.save()
            return Response(serializer.data)


# kunlik kelganlar
@api_view(['GET'])
def attendance_list(request):
    attendance = Attendance.objects.filter(came = True)
    serializer = AttendanceSerializer(attendance, many=True)
    return Response(serializer.data)