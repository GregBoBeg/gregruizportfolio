from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="gfolio-home" ),
    path('whyGreg/', views.whyGreg, name="whyGreg" ),
    path('bio/', views.bio, name="bio" ),
    path('portfolio/', views.portfolio, name="portfolio" ),

    path('project/<str:projectName>/', views.project, name='project')
]
