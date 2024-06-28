from django.shortcuts import render
from datetime import datetime as dt, timedelta as t
from django.http import HttpResponse


# Create your views here.


def currentDateTime(request):
    now = dt.now()
    formatted_now = now.strftime(' %I:%M:%S %p')
    return HttpResponse(
        f"<h1>Current Time is: </h1> {formatted_now}"
    )