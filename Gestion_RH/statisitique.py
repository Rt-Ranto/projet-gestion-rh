import numpy as np
from .models import Employe
from datetime import date, timedelta

class Statistique:
    def __init__(self, filtre):
        self.__filtre = filtre
            
    def nombre_homme_femme(self):
        if self.__filtre == 'Tout':
            nbrh = len(Employe.objects.filter(genre="Homme"))
            nbrf = len(Employe.objects.filter(genre="Femme"))
            total = Employe.objects.all().count()
        else:
            nbrh = len(Employe.objects.filter(unite=self.__filtre, genre="Homme"))
            nbrf = len(Employe.objects.filter(unite=self.__filtre, genre="Femme"))
            total = Employe.objects.filter(unite=self.__filtre).count()

        
        if total:
            return {
                'nbr_homme' : f"{nbrh}"if nbrh<1000 else f"{nbrh//1000}K",  
                'nbr_femme' : f"{nbrf}"if nbrf<1000 else f"{nbrf//1000}K",
                'nbr_homme_pourcentage': int(round((nbrh*100)/total,0)),
                'nbr_femme_pourcentage' : int(round((nbrf*100)/total,0)) 
             }
          
    def repartition_age(self):
        #__gt >à
        #__lt <à
        #__gte >= à
        #__lte <= à

        today = date.today()
        date_limite_25 = date(today.year - 25, today.month, today.day) #25 years ago
        date_limite_35 = date(today.year - 35, today.month, today.day) #25 years ago
        date_limite_45 = date(today.year - 45, today.month, today.day) #45 years ago
        date_limite_55 = date(today.year - 55, today.month, today.day) #55 years ago
        # date_limite_moins25 = date(today.year - 25, today.month, today.day)

        if self.__filtre == "Tout":
            total = Employe.objects.count()
            moins25 = Employe.objects.filter(date_naissance__gt = date_limite_25).count()#-25
            plus55 = Employe.objects.filter(date_naissance__lt = date_limite_55).count() #+55
            entre25_35 = Employe.objects.filter(
                    date_naissance__lte = date_limite_25,
                    date_naissance__gt= date_limite_35
            ).count()
            entre35_45 = Employe.objects.filter(
                    date_naissance__lte = date_limite_35,
                    date_naissance__gt= date_limite_45
            ).count()
            entre45_55 = Employe.objects.filter(
                    date_naissance__lte = date_limite_45,
                    date_naissance__gt= date_limite_55
            ).count()
            empl = Employe.objects.all()
            ages = [e.age() for e in empl]


        else:
            total = Employe.objects.filter(unite=self.__filtre).count()
            moins25 = Employe.objects.filter(unite=self.__filtre,date_naissance__gt = date_limite_25).count()#-25
            plus55 = Employe.objects.filter(unite=self.__filtre,date_naissance__lt = date_limite_55).count() #+55
            entre25_35 = Employe.objects.filter(
                unite=self.__filtre,
                date_naissance__lte = date_limite_25,
                date_naissance__gt= date_limite_35
            ).count()
            entre35_45 = Employe.objects.filter(
                unite=self.__filtre,
                date_naissance__lte = date_limite_35,
                date_naissance__gt= date_limite_45
            ).count()
            entre45_55 = Employe.objects.filter(
                unite=self.__filtre,
                date_naissance__lte = date_limite_45,
                date_naissance__gt= date_limite_55
            ).count()

            empl = Employe.objects.filter(unite=self.__filtre)
            ages = [e.age() for e in empl]

        if total:
            data = {
                "labels":["-25ans","25 à 35","35 à 45","45 à 55","+55ans"],
                "values":[moins25,entre25_35,entre35_45,entre45_55,plus55],
                "ages": ages,
                "moyenne": int(np.mean(ages)),
                "pourcentage":[
                    int((round(moins25*100/total,0) if total else 0)),
                    int((round(entre25_35*100/total,0) if total else 0)),
                    int((round(entre35_45*100/total,0) if total else 0)),
                    int((round(entre45_55*100/total,0) if total else 0)),
                    int((round(plus55*100/total,0) if total else 0))
                ]
            }
            return data 


    def repartition_grade(self):
        
        return {
                    "homme" : [
                        Employe.objects.filter(genre="Homme",categorie_grade="Haut gradé").count(),
                        Employe.objects.filter(genre="Homme", categorie_grade="Sous-officier").count(),
                        Employe.objects.filter(genre="Homme", categorie_grade="Militaire du rang").count()
                    ] if self.__filtre == "Tout" else[
                        Employe.objects.filter(unite=self.__filtre,genre="Homme",categorie_grade="Haut gradé").count(),
                        Employe.objects.filter(unite=self.__filtre, genre="Homme", categorie_grade="Sous-officier").count(),
                        Employe.objects.filter(unite=self.__filtre, genre="Homme", categorie_grade="Militaire du rang").count()
                    ],
                    "femme" : [
                        Employe.objects.filter(genre="Femme",categorie_grade="Haut gradé").count(),
                        Employe.objects.filter(genre="Femme", categorie_grade="Sous-officier").count(),
                        Employe.objects.filter(genre="Femme", categorie_grade="Militaire du rang").count()

                    ]if self.__filtre == "Tout" else[
                        Employe.objects.filter(unite=self.__filtre,genre="Femme",categorie_grade="Haut gradé").count(),
                        Employe.objects.filter(unite=self.__filtre, genre="Femme", categorie_grade="Sous-officier").count(),
                        Employe.objects.filter(unite=self.__filtre, genre="Femme", categorie_grade="Militaire du rang").count()
                    ]
                  
        }
        
        