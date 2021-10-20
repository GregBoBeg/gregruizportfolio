from django.urls import path
from . import views


urlpatterns = [
#   Match URL Paths and call related views for static web pages
    path('', views.index, name="gfolio-home" ),
    path('whyGreg/', views.whyGreg, name="whyGreg" ),
    path('bio/', views.bio, name="bio" ),
    path('portfolio/', views.portfolio, name="portfolio" ),
    path('qualifications/', views.qualifications, name="qualifications" ),

#   Match URL Paths and call related views for dynamicly-loaded project pages
    path('project/<str:projectName>/', views.project, name='project')
]
