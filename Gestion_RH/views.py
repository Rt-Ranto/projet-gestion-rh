

import os,csv,shutil,getpass
import pandas as pd
import base64

from datetime import datetime

from weasyprint import HTML, CSS
from io import TextIOWrapper
from django.shortcuts import render, redirect, get_object_or_404 
from django.http import request, HttpResponse
from Gestion_RH.models import User
from django.db.models import Q
from django.contrib.auth import authenticate, logout as auth_logout,login as auth_login
from django.conf import settings
from django.template.loader import render_to_string
from django.templatetags.static import static
from .getDataJson import DataJson
from .models import Employe
from .statisitique import Statistique
from .recherch import Recherch

from django.core.cache import cache
from django.http import HttpResponse

def clear_cache(request):
    cache.clear()
    return HttpResponse("Cache vidé")

def se_connecter(request):
    error_username = None
    error_password = None

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        if username != "" and password != "":
            #trouver si le ueername existe
            if not User.objects.filter(username=username).exists():
                error_username = "Cette Admin n'existe pas"

            else:
                #si le username existe , verifier où est l'erreur
                user = authenticate(username=username,password=password)


                if user is None:
                    error_password = "mode de passe incorrect"

                else:
                    auth_login(request, user)
                    return redirect('home')
        else:
            if password != "" and username == "":
                error_username = "completer le champ Admin"
            if password == "" and username != "":
                error_password = "completer le champ mot de passe"

    return render(request, 'Authentification/login.html',{
        'error_username' : error_username,
        'error_password' : error_password
    })

def home(request):
    user = User.objects.all()
    d_json = DataJson()
    d = d_json.lire_json_data()
    s = Statistique(d['filtre'])
    if d['recherch_query'] == "":
        if d['filtre'] == "Tout":
            if d['order'] == "croissant":
                employe = Employe.objects.all().order_by(f"{d['sort']}")
            else:
                employe = Employe.objects.all().order_by(f"-{d['sort']}")
        else:
            if d['order'] == "croissant":
                employe = Employe.objects.filter(unite=d['filtre']).order_by(f"{d['sort']}")
            else:
                employe = Employe.objects.filter(unite=d['filtre']).order_by(f"-{d['sort']}")
    
    else:
        r = Recherch(d['recherch_query'])
        employe = r.recherch_employe()
        d_json.ecrire_json_data(
            {
                "filtre":d['filtre'],
                "sort":d['sort'],
                "order":d['order'],
                "recherch_query": ""
            }
        )
    unite = Employe.objects.values_list("unite", flat=True).distinct()
    return render(request, "Content/home.html",
        {
        'employe' : employe,
        'username': user,
        'unite':unite,
        'filtre' : d['filtre'],
        'sort': d['sort'],
        'total' : len(employe),
        's_sexe': s.nombre_homme_femme(),
        'pie_data': s.repartition_age(),
        'bar_data':s.repartition_grade()
        }
    )

def filtre(request, u:str):
    user = User.objects.all()
    d_json = DataJson()
    d = d_json.lire_json_data()
    n_d = {
        "filtre":u,
        "sort": d['sort'],
        "order": d['order'],
        "recherch_query": d['recherch_query']
    }
    d_json.ecrire_json_data(n_d)
    return redirect('home')
    
    

def trie(request, t:str):
    d_json = DataJson()
    d = d_json.lire_json_data()
    n_d = {
        "filtre":d['filtre'],
        "sort": t,
        "order": d['order'],
        "recherch_query": d['recherch_query']
    }
    d_json.ecrire_json_data(n_d)
    return redirect('home')

def order(request, o:str):
    d_json = DataJson()
    d = d_json.lire_json_data()
    n_d = {
        "filtre":d['filtre'],
        "sort": d['sort'],
        "order": o,
        "recherch_query": d['recherch_query']
    }
    d_json.ecrire_json_data(n_d)
    return redirect('home')

def logout(request):
    auth_logout(request)
    return redirect('login')

def ajouter(request):
    return render(request,"Content/ajouter.html")

def ajouter_employer(request):
    if request.method == "POST":
        if request.POST.get("form_name") == "form1":
            try:
                Employe.objects.create(
                    nom=request.POST.get('nom').upper(),
                    prenom=request.POST.get('prenom').capitalize(),
                    date_naissance=request.POST.get('date_naissance'),
                    genre=request.POST.get('genre'),
                    pere=request.POST.get('pere'),
                    mere=request.POST.get('mere'),
                    situation_maritale=request.POST.get('situation_maritale'),
                    diplome_experience=request.POST.get('diplome_experience'),
                    adresse=request.POST.get('adresse'),
                    email=request.POST.get('email'),
                    telephone=request.POST.get('telephone'),
                    unite=request.POST.get('unite'),
                    grade=request.POST.get('grade'),
                    unite_ancien=request.POST.get('unite_ancien'),
                    matricule=request.POST.get('matricule'),
                    date_embauche=request.POST.get('date_embauche'),
                    photo=request.FILES.get('photo')
                )
                photo=request.FILES.get('photo')
                print(photo)
                return redirect('reussie')

            except Exception as e:
                return render(request, 'Content/ajouter.html', {
                    'error': e
                })

    return render(request, 'Content/ajouter.html')

def ajouter_par_csv(request):
    if request.method == 'POST':
        csv_file = request.FILES.get("csv_file")
        df = pd.read_csv(csv_file)
        df.dropna(inplace=True)
        username = getpass.getuser()
        for x in df.index:
            source_path_photo = f"C:/Users/{username}/Pictures/{df.loc[x,'photo']}"
            destination_path_photo = os.path.join(settings.MEDIA_ROOT,"employe")
            os.makedirs(destination_path_photo,exist_ok = True)
            shutil.copy(source_path_photo, destination_path_photo)

            Employe.objects.create(
                nom=df.loc[x,'nom'].upper(),
                prenom=df.loc[x,'prenom'].capitalize(),
                date_naissance=df.loc[x,'date_naissance'],
                genre=df.loc[x,'genre'],
                pere=df.loc[x,'pere'] or None,
                mere=df.loc[x,'mere'] or None,
                situation_maritale=df.loc[x,'situation_maritale'],
                diplome_experience=df.loc[x,'diplome_experience'],
                adresse=df.loc[x,'adresse'],
                email=df.loc[x,'email'] or None,
                telephone=int(df.loc[x,'telephone']),
                unite=df.loc[x,'unite'],
                grade=df.loc[x,'grade'],
                unite_ancien=df.loc[x,'unite_ancien'],
                matricule=int(df.loc[x,'matricule']),
                date_embauche=df.loc[x,'date_embauche'],
                photo="employe/" + df.loc[x,'photo'],  
            )
        return redirect("reussie")

def reussie(request):
    return render(request,'Content/reussie.html')
    
def pdf(request):
    return render(request, "Content/exportPdf.html",{
        "e": get_object_or_404(Employe,id=4221),
        "age": 35
    })

def rechercher(request):
    d_json = DataJson()
    d = d_json.lire_json_data()
    if request.method == "POST":
        query = request.POST.get('recherch')
        if query:

            if query == "tout":
                d_json.ecrire_json_data(
                    {
                        "filtre":"Tout",
                        "sort":d['sort'],
                        "order":d['order'],
                        "recherch_query":""
                    }
                )
                return redirect('home')

            elif query == "clear_all_db":
                Employe.objects.all().delete()
                return redirect('home')
            
            else:
                d_json.ecrire_json_data(
                    {
                        "filtre":d['filtre'],
                        "sort":d['sort'],
                        "order":d['order'],
                        "recherch_query":query
                    }
                )
                return redirect('home')
            
        else:
            return redirect('home')
    
        

def modifier(request, id):
     employe = get_object_or_404(Employe, id=id)
     try:
        if request.method == "POST":
           employe.nom=request.POST.get('nom').upper()
           prenom = request.POST.get('prenom')
           employe.prenom = prenom[0].upper() + prenom[1:].lower() 
           employe.date_naissance=request.POST.get('date_naissance')
           employe.genre=request.POST.get('genre')
           employe.pere=request.POST.get('pere')
           employe.mere=request.POST.get('mere')
           employe.situation_maritale=request.POST.get('situation_maritale')
           employe.diplome_experience=request.POST.get('diplome_experience')
           employe.adresse=request.POST.get('adresse')
           employe.email=request.POST.get('email')
           employe.telephone=request.POST.get('telephone')
           employe.unite=request.POST.get('unite')
           employe.grade=request.POST.get('grade')
           employe.unite_ancien=request.POST.get('unite_ancien')
           employe.matricule=request.POST.get('matricule')
           employe.date_embauche=request.POST.get('date_embauche')
           photo = request.FILES.get('photo')
           if employe.photo and photo:
                if os.path.isfile(employe.photo.path):
                    os.remove(employe.photo.path)
                    employe.photo = photo
                else:
                    employe.photo= photo
           
           employe.save() #mise à jour
           return redirect('home')

     except Exception as e:
                return render(request, 'Content/modifier.html', {
                    'employe':employe,
                    'error': e
                })

     return render(request,"Content/modifier.html",{'employe':employe})

def supprimer(request, id):
    employe = get_object_or_404(Employe, id=id)
    employe.delete()
    if employe.photo:
        if os.path.isfile(employe.photo.path):
            os.remove(employe.photo.path)

    return redirect('home')

def voir(request, id):
    employe = get_object_or_404(Employe,id=id)
    
    return render(request, 'Content/voir.html',{
        'e':employe,
        'age':employe.age()
    })


def export_pdf(request, emp_id):
    
    e = get_object_or_404(Employe, id=emp_id)
     # Utiliser BASE_DIR directement
    base_dir = settings.BASE_DIR
    
    # Chemins vers vos fichiers
    logo_path = os.path.join(base_dir,'Gestion_RH','static','Gestion_RH' ,'img', 'R.png')
    photo_path = os.path.join(base_dir, 'media', f'{e.photo}')
    
    # Vérifier que les fichiers existent
    print(f"Logo path: {logo_path}")
    print(f"Logo existe: {os.path.exists(logo_path)}")
    print(f"Photo path: {photo_path}")
    print(f"Photo existe: {os.path.exists(photo_path)}")
    # Encoder les images
    logo_base64 = None
    if os.path.exists(logo_path):
        with open(logo_path, 'rb') as f:
            logo_base64 = base64.b64encode(f.read()).decode('utf-8')
    
    photo_base64 = None
    if os.path.exists(photo_path):
        with open(photo_path, 'rb') as f:
            photo_base64 = base64.b64encode(f.read()).decode('utf-8')


    context = {
        'e':e,
        'age':e.age,
        'logo_base64':logo_base64,
        'photo_base64':photo_base64
    }
    
    css_path = os.path.join(base_dir,"Gestion_RH","static","Gestion_RH","css","exportPdfStyle.css")
    print(f"css path : {css_path}")
    print(f"css path exist: {os.path.exists(css_path)}")
    
    # Appliquer le CSS
    
    html_string = render_to_string('Content/exportPdf.html', context)
    html = HTML(string=html_string, base_url=request.build_absolute_uri())
    # pdf = html.write_pdf()
    pdf = html.write_pdf(stylesheets=[CSS(filename=css_path)])

    response = HttpResponse(pdf, content_type='application/pdf')
    
    titre = "Mr" if e.genre == "Homme" else "Mme"

    filename = f"{titre} {e.nom} {e.prenom}.pdf"
    response['Content-Disposition'] = f'attachment; filename="{filename}"'

    # Pour permettre à fetch() de lire les headers
    response['Access-Control-Expose-Headers'] = 'Content-Disposition'
    
    return response

def ajouter_par_pdf(request):
    if request.method == "POST":
        file = request.POST.get("pdf_file")

        if file:
            pass

def conge(request):
    return render(request, "Content/conge.html")