from django.db import models
from django.contrib.auth.models import User
# Create your models here.
#modelisation de la classe etudiant avec heritage de la classe User       
class Etudiant(models.Model):
    #code de l'héritage 
    user= models.OneToOneField(User,on_delete=models.CASCADE)
    Niveau=models.CharField(max_length=20)
    Matricule=models.CharField(max_length=15 ,unique = True)
    def __str__(self):
        return self.user.username
#modelisation de la classe administrateur avec heritage de la classe etudiant
class Admin(models.Model):
    userA = models.OneToOneField(Etudiant,on_delete=models.CASCADE)
    role = models.CharField(max_length=20)
    def __str__(self):
        return f"administrateur {self.userA.user.username}"
#créons une classe eleve


    

    
    
    