from django.shortcuts import render

# Create your views here.
def displayFruits(request):
    fruits = ['Apple', 'Bannana', 'Cranberry', 'Dragon Fruit','Orange']

    return render(request, 'lists/fruits.html', {'fruits': fruits})

def displayStudents(request):
    students = ['Student-1','Student-2','Student-3','Student-4','Student-5']

    return render(request, 'lists/students.html', {'students': students})