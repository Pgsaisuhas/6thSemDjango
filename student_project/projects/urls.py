from django.urls import path
from .views import project_create_view, success_view

urlpatterns = [
    path('projects/', project_create_view, name='create_project'),
    path('success/', success_view, name='success'),
]
