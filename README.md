# 🚀 GRH-Admin

> **Statut :** En cours de développement (60%)

## 📝 Description
Application web de Gestion des personnels , des flux de congé et repos 
ainsi la repartition des departements dans une entreprise ou etablissement*

## ✨ Fonctionnalités
- [x] Interface pour l'administration (HTML/CSS/JavaScript + Bootstrap5)
- [x] Gestion des données du personnel (Django + postgreSQL)
- [x] Affichage par graph de la repartition des personnels (Chart.js)
- [x] Système d'authentification des utilisateurs
- [x] Recherch et filtre des personnels 
- [x] Modification,Suppression d'une employé 
- [x] Ajout d'une simple employé
- [x] Ajout multiple de plusieurs personnels via fichier Excel
- [x] Eportation en pdf des informations personnels d'une employé
- [ ] Modification de l'admin (À venir)
- [ ] Gestion des Congés et Repos (À venir)
- [ ] Envoyer des emails à tous les personnels(À venir)

## 🛠️ Technologies utilisées
- **Frontend :**HTML/CSS, JavaScript, Bootstrap5, FontAwesome
- **Backend :** Django, Python-dotenv, pandas, weasyprint
- **Base de données :** PostgreSql
- **Grapth :** Chart.js

## 📸 Aperçu
<img width="1366" height="766" alt="GRH Admin - Google Chrome 17_03_2026 17_26_29" src="https://github.com/user-attachments/assets/c937144e-e014-46f8-bff3-0c1d07ddaffc" />
<img width="1366" height="768" alt="GRH Admin - Google Chrome 17_03_2026 18_34_37" src="https://github.com/user-attachments/assets/3dc47e85-3c07-485f-8b8b-51a1f7a4680f" />
<img width="1366" height="766" alt="GRH Admin - Google Chrome 17_03_2026 17_24_38" src="https://github.com/user-attachments/assets/b54d273d-a06e-4b6b-9ae7-623f89b006e4" />
<img width="1366" height="766" alt="GRH Admin - Google Chrome 17_03_2026 17_24_48" src="https://github.com/user-attachments/assets/0a9e18a8-c2ae-4cac-bb21-f38c7632ed2f" />
<img width="1366" height="766" alt="GRH Admin - Google Chrome 17_03_2026 17_25_36" src="https://github.com/user-attachments/assets/b4599896-57fd-4c7e-8b1f-c95399f63851" />



## ⚙️ Installation
1. Cloner le projet : `git clone [URL]`
2. Lancer l'environnement : `pipenv shell`
3. Migrer la base de donneé : `pyhton manage.py migrate puis pyhton manage.py makemigrations`
4. Créer un superUser : `python manage.py createsuperuser puis remplisser username, email, password`
5. Configurer .env voir le .env.example
6. Lancer le server : `python manage.py runserver`
7. Connecter avec le superUser

