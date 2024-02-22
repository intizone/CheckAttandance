from .models import Staff, Attendance
from django.urls import path 

app_name = 'main'

urlpatterns = [
    path('stuff/', Staff, name='stuff-list'),
    path('attendance/', Attendance, name='attendance-list')
]