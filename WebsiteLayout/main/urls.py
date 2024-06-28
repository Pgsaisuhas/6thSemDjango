from django.urls import path
from . import views
urlpatterns = [
    path('home/', views.home, name="home"),
    path('about-us/', views.aboutUs, name='about-us'),
    path('contact-us/', views.contactUs, name="contact-us"),
]
