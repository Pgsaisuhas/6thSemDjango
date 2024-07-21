from django.views.generic import ListView, DetailView
from .models import Student


class StudentListView(ListView):

    model = Student
    template_name = 'generic/student_list.html'
    context_object_name = 'students'


class StudentDetailView(DetailView):
    model = Student
    template_name = 'generic/student_detail.html'
    context_object_name = 'student'