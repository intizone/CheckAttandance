from django.urls import path
from . import views

app_name = 'api'

urlpatterns = [
    path('staff-list/', views.staff_list, name='staff-list'),
    path('staff-create/', views.staff_create, name='staff-create'),
    path('attendance-create/', views.attendance_create, name='attendance-create'),
    path('attendance-list/', views.attendance_list, name='attendance-list'),
]