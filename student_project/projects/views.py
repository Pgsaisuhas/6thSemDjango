from django.shortcuts import render, redirect
from .forms import ProjectForm

# Create your views here.

def project_create_view(request):
    if request.method == 'POST':
        form  = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = ProjectForm()
    
    return render(request, 'projects/project_form.html', {'form': form})

def success_view(request):
    return render(request, 'projects/success.html')