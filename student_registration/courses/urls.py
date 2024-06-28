from django.urls import path
from . import views
urlpatterns = [
    path('student-registration/', views.register_student, name="student_registration"),
    path('course-details/<int:course_id>/', views.course_details, name="course-details"),
    path('course-list/', views.course_list, name="course-list"),
]
