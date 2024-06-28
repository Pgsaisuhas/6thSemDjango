from django.urls import path
from .views import currentDateTime


urlpatterns = [
    path('', currentDateTime, name="cdt"),
]