from django.shortcuts import render
from datetime import datetime as dt, timedelta as t
from django.http import HttpResponse


# Create your views here.

#Mod1 exp 1
def currentDateTime(request):
    now = dt.now()
    formatted_now = now.strftime(' %I:%M:%S %p')
    return HttpResponse(
        f"<h1>Current Time is: </h1> {formatted_now}"
    )

#Mod1 exp 2
def beforeCurrentAfter(request):
    now = dt.now()
    before = now - t(hours=4)
    after = now + t(hours=4)
    context = {
        'formatted_date': now.date(),
        'formatted_now': now.strftime('%I:%M:%S %p'),
        'formatted_before': before.strftime('%I:%M:%S %p'),
        'formatted_after': after.strftime('%I:%M:%S %p'),
    }
    return render(request, 'cdt/beforeCurrentAfter.html', context)
