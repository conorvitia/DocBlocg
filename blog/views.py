from django.shortcuts import render,redirect
from .models import *
from .forms import InscriptionForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def accueil(request):
    context = {
        'nom':'mvondo',
        'age': 25,
        'couleurs': ['rouge', 'vert', 'bleu'],
        'est_connecte': True,
    }    
    return render (request,'home.html',context)

from django.shortcuts import render, redirect
from .forms import InscriptionForm

def inscription(request):
    if request.method == "POST":
        form = InscriptionForm(request.POST)
        if form.is_valid():
            # Création de l'objet sans sauvegarde immédiate en DB
            user = form.save(commit=False)
            # Récupération sécurisée du mot de passe via le dictionnaire
            mot_de_passe = form.cleaned_data.get('pwd')
            # Cryptage du mot de passe (IMPORTANT)
            user.set_password(mot_de_passe)
            user.save()
            # redirection vers la page d'accueil après inscription réussie
            return redirect('accueil') 
    else:
        # Formulaire vide pour une requête GET
        form = InscriptionForm()
    return render(request, 'contact.html', {'form': form})

def to(request):
    if request.method=="POST":
        form=InscriptionForm(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            user.set_password(form.cleaned_data.get("pwd"))
            user.save()
            return redirect('projet.html')
    else:
             form=InscriptionForm(request.POST)
    return render ( request,'contact.html',{'form':form})

def connexion(request):
     if request.method == 'POST':
         #récupération du nom de l'utilisateur
        username = request.POST['username']
        #récupération du mot de passe
        password = request.POST['password']
        #authentification avec la fonctio authenticate de django
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('accueil')
        else:
            messages.error(request, 'Nom d\'utilisateur ou mot de passe incorrect.')
     return render (request,"connexion.html")
 #fonction de déconnexion qui utilise la fonction logout de django pour déconnecter 
 # l'utilisateur et redirige vers la page d'accueil
def deconnexion(request):
    logout(request)
    return redirect('accueil')