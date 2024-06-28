from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'main/home.html')

def aboutUs(request):
    return render(request, 'main/aboutUs.html')

def contactUs(request):
    contacts = ['Contact - 1', 'Contact - 2','Contact - 3','Contact - 4']
    context = {
        'contacts': contacts,
    }
    return render(request, 'main/contactUs.html', context)