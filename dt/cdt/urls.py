from django.urls import path
from .views import currentDateTime, beforeCurrentAfter


urlpatterns = [
    path('cdt/', currentDateTime, name="cdt"),
    path('', beforeCurrentAfter, name="bca")
]