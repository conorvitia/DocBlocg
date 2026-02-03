from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [ 
               path('', views.accueil, name='accueil'),
               path('contact/',views.inscription, name='inscription'),
               path('message_list/',views.secondformulaire_view, name='message_list')
               ]
    