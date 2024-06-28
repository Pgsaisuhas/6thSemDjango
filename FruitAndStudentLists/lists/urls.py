from django.urls import path
from .views import displayFruits, displayStudents
urlpatterns = [
    path('fruits/', displayFruits, name="fruits"),
    path('students/', displayStudents, name="students"),
]
