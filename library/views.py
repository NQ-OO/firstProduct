from django.shortcuts import render

# Create your views here.


def landingPage(request) :
    return render(request, 'library/landingPage.html')

def library(request):
    return render(request, 'library/library.html')

def collectHighlight(request):
    return render(request, 'library/collectHighlight.html')

def editor(request):
    return render(request, 'library/editor.html')

def viewer(request):
    return render(request, 'library/viewer.html')

