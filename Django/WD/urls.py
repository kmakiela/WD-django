
from django.urls import path

from . import views

urlpatterns = [
    path('students/<str:name>/', views.show_student_info, name='Find birthdate od student'),
    path('students/', views.show_all_students, name="all students"),
    path('courses/', views.show_all_courses, name='Displays all courses'),
    path('courses/<str:topic>/', views.show_course_info, name='Shows course info'),
    path('', views.main_view_wd, name="main page"),

]