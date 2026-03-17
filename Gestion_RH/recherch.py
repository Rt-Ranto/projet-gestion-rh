from django.db.models import Q
from .models import Employe

class Recherch:
    def __init__(self,query:str):
        self.__query = query.split()

    def recherch_employe(self):
        if len(self.__query) == 1:
            employe = Employe.objects.all().filter(
                Q(nom__icontains = self.__query[0])|
                Q(prenom__icontains = self.__query[0])|
                Q(matricule__icontains = self.__query[0])|
                Q(date_naissance__icontains = self.__query[0])|
                Q(situation_maritale__icontains = self.__query[0])|
                Q(unite__icontains = self.__query[0])|
                Q(grade__icontains = self.__query[0])|
                Q(unite_ancien__icontains = self.__query[0])|
                Q(email__icontains = self.__query[0])|
                Q(telephone__icontains = self.__query[0])|
                Q(adresse__icontains = self.__query[0])|
                Q(genre__icontains = self.__query[0])|
                Q(nom__icontains = self.__query[0])|
                Q(diplome_experience__icontains = self.__query[0])
                )
        elif len(self.__query)==2:
            employe = Employe.objects.all().filter(
                Q(nom__icontains = self.__query[0], prenom__icontains = self.__query[1])|
                Q(nom__icontains = self.__query[1], prenom__icontains = self.__query[0])|
                Q(nom__icontains = self.__query[1], unite__icontains = self.__query[0])|
                Q(nom__icontains = self.__query[0], unite__icontains = self.__query[1])|
                Q(prenom__icontains = self.__query[1], unite__icontains = self.__query[0])|
                Q(prenom__icontains = self.__query[0], unite__icontains = self.__query[1])|
                Q(nom__icontains = self.__query[1], grade__icontains = self.__query[0])|
                Q(nom__icontains = self.__query[0], grade__icontains = self.__query[1])|
                Q(prenom__icontains = self.__query[1], grade__icontains = self.__query[0])|
                Q(prenom__icontains = self.__query[0], grade__icontains = self.__query[1])|
                Q(genre__icontains = self.__query[1], grade__icontains = self.__query[0])|
                Q(genre__icontains = self.__query[0], grade__icontains = self.__query[1])|
                Q(genre__icontains = self.__query[1], unite__icontains = self.__query[0])|
                Q(genre__icontains = self.__query[0], unite__icontains = self.__query[1])
                )
        elif len(self.__query) == 3 :
            employe = Employe.objects.all().filter(
                Q(nom__icontains = self.__query[0], prenom__icontains = self.__query[1], unite__icontains = self.__query[2])|
                Q(nom__icontains = self.__query[1], prenom__icontains = self.__query[0], unite__icontains = self.__query[2])
            )

        return employe