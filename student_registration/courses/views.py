from django.shortcuts import render
from .models import Course, Student
# Create your views here.
def register_student(request):
    if request.method == 'POST':
        student_name = request.POST.get('student_name')
        course_id = request.POST.get('course_id')
        course = Course.objects.get(pk=course_id)
        student = Student.objects.create(name=student_name)
        student.courses.add(course)
    courses = Course.objects.all()

    return render(request, 'courses/register_student.html', {'courses':courses})


def course_details(request, course_id):
    course = Course.objects.get(pk=course_id)
    students = course.students.all()

    return render(request, 'courses/course_details.html', {'course':
    course, 
    'students':students})


def course_list(request):
    courses = Course.objects.all()
    return render(request, 'courses/course_list.html', {'courses': courses})