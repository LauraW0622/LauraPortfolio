from django.shortcuts import render

# Create your views here.
def home(request): 
    return render(request, 'index.html')

def gallery(request): 
    return render(request, 'gallery.html')

def resume(request):
    return render(request, 'resume.html')

def projects(request):
    return render(request, 'projects.html')

def corpus(request): 
    return render(request, 'corpus.html')