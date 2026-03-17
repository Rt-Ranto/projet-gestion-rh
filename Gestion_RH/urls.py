from django.urls import path
from . import views

urlpatterns = [
    path('',views.se_connecter,name="index"),
    path('login',views.se_connecter,name="login"),
    path('home', views.home,name="home"),
    path('logout', views.logout,name="logout"),
    path('ajouter', views.ajouter,name="ajouter"),
    path('reussie',views.reussie,name="reussie"),
    path('conge', views.conge,name="conge"),
    path('ajouter_employer', views.ajouter_employer, name='ajouter_employer'),
    path('ajouter_par_csv', views.ajouter_par_csv, name='ajouter_par_csv'),
    path('ajouter_par_pdf', views.ajouter_par_pdf, name='ajouter_par_pdf'),
    path('rechercher', views.rechercher,name='rechercher'),
    path('pdf', views.pdf, name='pdf'),
    path("clear-cache/", views.clear_cache),
    path('export_pdf/<int:emp_id>/', views.export_pdf,name='export_pdf'),
    path('modifier/<int:id>/', views.modifier,name='modifier'),
    path('supprimer/<int:id>/', views.supprimer,name='supprimer'),
    path('voir/<int:id>/', views.voir,name='voir'),
    path('filtre/<str:u>/', views.filtre,name='filtre'),
    path('trie/<str:t>/', views.trie,name='trie'),
    path('order/<str:o>/', views.order,name="order")
]