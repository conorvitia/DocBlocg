from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [ 
    path('', views.accueil, name='accueil'),
    path('inscription/', views.inscription, name='inscription'), # Modifié 'contact/' en 'inscription/'
    path('connexion/', views.connexion, name='connexion'),       # Modifié 'message/' en 'connexion/'
]
