from django.urls import path, re_path

from . import views

urlpatterns = [
    path('csv/', views.csv_build, name="csv-build"),
    path('pdf/', views.pdf_build, name="pdf-build")
]
