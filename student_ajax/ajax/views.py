from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Course, Student

@csrf_exempt
def registration(request):
    if request.method == 'POST':
        student_id = request.POST.get('s_name')
        course_id = request.POST.get('c_name')

        try:
            student = Student.objects.get(id=student_id)
            course = Course.objects.get(id=course_id)
        
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)

        if student.enrollment.filter(id=course_id).exists():
            return JsonResponse({"message": "Student Already Enrolled!"}, status=200)
        
        student.enrollment.add(course)
        return JsonResponse({"message": "Student Enrolled Successfully!"}, status=200)
    else:
        students = Student.objects.all()
        courses = Course.objects.all()
        return render(request, 'ajax/register.html', {"students": students, "courses": courses})

def get_enrollments(request):
    students = Student.objects.all()
    enrollments = []
    for student in students:
        enrolled_courses = student.enrollment.all()
        courses = [course.course_name for course in enrolled_courses]
        enrollments.append({
            "student_name": student.student_name,
            "courses": ", ".join(courses)
        })
    return JsonResponse({"enrollments": enrollments})