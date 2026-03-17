from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    photo = models.ImageField(
        upload_to = 'users/',
        null = True,
        blank = True
    )
    
    def __str__(self):
        return self.username

class Employe(models.Model):
    nom = models.CharField(max_length=250, null=False, blank=False)
    prenom = models.CharField(max_length=250, null=False, blank=False)
    date_naissance = models.DateField(null=False)
    genre = models.CharField(max_length=6,null=False, blank=False)
    pere = models.CharField(max_length=500,null=True,blank=True)
    mere = models.CharField(max_length=500,null=True,blank=True)
    situation_maritale = models.CharField(max_length=15, null=False, blank=False)
    diplome_experience = models.TextField(null=False, blank=False)
    adresse = models.CharField(max_length=300,null=False)
    email = models.EmailField(unique=True, null=True, blank=True)
    telephone = models.IntegerField(null=False, blank=False)
    unite = models.CharField(max_length=250, null=False, blank=False)
    grade = models.CharField(max_length=250, null=False, blank=False)
    categorie_grade = models.CharField(
        max_length=20,
        choices=[
            ("Haut gradé", "Haut gradé"),
            ("Sous-officier", "Sous-officier"),
            ("Militaire du rang", "Militaire du rang"),
        ],
        default="Militaire du rang",
        editable=False
    )
    unite_ancien = models.CharField(max_length=250,null=False, blank=False)
    matricule = models.IntegerField(unique=True, null=False, blank=False)
    date_embauche = models.DateField(null=False)
    date_ajout = models.DateField(auto_now_add=True)
    photo = models.ImageField(
        upload_to = 'employe/',
        null = False,
        blank = False,
        unique=False
    )

    def __str__(self):
        return f"{self.nom} {self.prenom} Marticule {self.matricule}"

    def age(self):
        today = timezone.now().date()
        age = today.year - self.date_naissance.year
        if (today.month, today.day) < (self.date_naissance.month, self.date_naissance.day):
            age -= 1

        return age

    def save(self, *args, **kwargs):
        HAUT_GRADE = [
            "General", "Colonel", "Lieutenant-colonel",
            "Commandant", "Capitaine", "Lieutenant", "Sous-lieutenant"
        ]

        SOUS_OFFICIER = [
            "Adjudant-chef", "Adjudant", "Sergent-chef", "Sergent"
        ]

        if self.grade in HAUT_GRADE:
            self.categorie_grade = "Haut gradé"
        elif self.grade in SOUS_OFFICIER:
            self.categorie_grade = "Sous-officier"
        else:
            self.categorie_grade = "Militaire du rang"

        super().save(*args, **kwargs)
