from django.urls import path
from . import views


urlpatterns = [
#   Match URL Paths and call related views for static web pages
    path('', views.index, name="gfolio-home" ),
    path('whyGreg/', views.whyGreg, name="whyGreg" ),
    path('bio/', views.bio, name="bio" ),
    path('credibility/', views.credibility, name="credibility" ),
    path('portfolio/', views.portfolio, name="portfolio" ),
    path('nonomedia/', views.project_nonomedia, name="project-nonomedia" ),
    path('doneez/', views.project_doneez, name="project-doneez" ),
    path('qualifications/', views.qualifications, name="qualifications" ),
    path('project/gmart', views.project_gmart, name="project-gmart" ),
    path('project/gtalk', views.project_gtalk, name="project-gtalk" ),
    path('project/vivix', views.project_vivix, name="project-vivix" ),
    path('project/buzzreport', views.project_buzzreport, name="project-buzzreport" ),
    path('project/past', views.project_past, name="project-past" ),

]
