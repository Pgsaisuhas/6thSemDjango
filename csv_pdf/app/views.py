import csv
from .models import Course
from django.http import HttpResponse
from django.http import HttpResponse
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle


def csv_build(request):
    courses = Course.objects.all()
    response = HttpResponse(content_type="text/csv")
    response['Content-Disposition'] = 'attachment; filename="Course_List.csv"'
    writer = csv.writer(response)
    writer.writerow(['Course Code', 'Course Name', 'Course Credits'])

    for course in courses:
        writer.writerow([course.course_code, course.course_name, course.course_credits])
    
    return response



def pdf_build(request):
    # Create the HttpResponse object with the appropriate PDF headers.
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="Course_List.pdf"'

    # Create the PDF object, using the response object as its "file."
    doc = SimpleDocTemplate(response, pagesize=letter)
    
    # Container for the 'Flowable' objects.
    elements = []

    # Data for the table.
    courses = Course.objects.all()
    data = [['Course Code', 'Course Name', 'Credits']]  # Header row
    for course in courses:
        data.append([course.course_code, course.course_name, str(course.course_credits)])

    # Create the table with data.
    table = Table(data)
    
    # Add style to the table.
    style = TableStyle([
        # ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.black),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 12),
        # ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        # ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ])
    table.setStyle(style)

    # Add the table to the elements list.
    elements.append(table)

    # Build the PDF.
    doc.build(elements)

    return response

