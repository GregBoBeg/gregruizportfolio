from django.shortcuts import render

#   Route to static web pages

def index(request):
    return render(request, 'gfolio_app/index.html')

def whyGreg(request):
    return render(request, 'gfolio_app/whyGreg.html')

def bio(request):
    return render(request, 'gfolio_app/bio.html')

def portfolio(request):
    return render(request, 'gfolio_app/portfolio.html')

#   Route to dynamicly-loaded project pages

def project(request, projectName):
    context = {"projectName": projectName}
    return render(request, 'gfolio_app/project.html', context)