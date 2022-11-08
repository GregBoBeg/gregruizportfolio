from django.shortcuts import render

#   Route to static web pages

def index(request):
    return render(request, 'gfolio_app/index.html')

def qualifications(request):
    return render(request, 'gfolio_app/my-qualifications.html')

def whyGreg(request):
    return render(request, 'gfolio_app/my-whyMe.html')

def bio(request):
    return render(request, 'gfolio_app/my-bio.html')

def credibility(request):
    return render(request, 'gfolio_app/my-credibility.html')

def portfolio(request):
    return render(request, 'gfolio_app/portfolio.html')

def project_nonomedia(request):
    return render(request, 'gfolio_app/project-nonomedia.html')

def project_doneez(request):
    return render(request, 'gfolio_app/project-doneez.html')

def project_gmart(request):
    return render(request, 'gfolio_app/project-gmart.html')

def project_gtalk(request):
    return render(request, 'gfolio_app/project-gtalk.html')

def project_vivix(request):
    return render(request, 'gfolio_app/project-vivix.html')

def project_buzzreport(request):
    return render(request, 'gfolio_app/project-buzzreport.html')

def project_past(request):
    return render(request, 'gfolio_app/project-past.html')

