from django.shortcuts import render

def index(request):
    return render(request, 'gfolio_app/index.html')

def whyGreg(request):
    return render(request, 'gfolio_app/whyGreg.html')

def bio(request):
    return render(request, 'gfolio_app/bio.html')


def project(request, projectName):
    context = {"projectName": projectName}
    return render(request, 'gfolio_app/project.html', context)