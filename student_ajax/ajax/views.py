from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.template.loader import render_to_string
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
        table_html = get_enrollments()
        
        return JsonResponse({
            "message": "Student Enrolled Successfully!",
            "tableHtml": table_html
        }, status=200)
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
    return render_to_string('ajax/student_table.html', {"enrollments": enrollments})

def course_search(request):
    if request.method == 'POST':
        course_id = request.POST.get('c_name')
        
        # Filter students by course_id
        student_list = Student.objects.filter(enrollment__id=course_id)
        
        if not student_list.exists():
            return HttpResponse("<h1>No Student Enrolled</h1>")
        
        return render(request, 'ajax/student_list.html', context={"student_list": student_list})
    
    else:
        courses = Course.objects.all()
        return render(request, 'ajax/course_search.html', {"courses": courses})
        