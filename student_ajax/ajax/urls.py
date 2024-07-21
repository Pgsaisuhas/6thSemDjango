from django.urls import path
from . import views
urlpatterns = [
    path('register/', views.registration, name="regitration"),
    path('get_enrollments/', views.get_enrollments, name="enrollments")
]
