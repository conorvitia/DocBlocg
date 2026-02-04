from django.shortcuts import render,redirect
from .models import *
from .forms import InscriptionForm

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
            # Assurez-vous que 'projet.html' est bien le NOM de votre URL (path name)
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
    return render (request,"connexion.html")
