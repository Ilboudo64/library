📚 Gestion de Bibliothèque - Django Kata
Ce projet est une application complète de gestion de bibliothèque développée avec Django 6.0. Elle permet de gérer le cycle de vie des livres, des lecteurs et des réservations, tout en offrant une interface de programmation (API) pour des extensions futures (mobile/web).

🚀 Fonctionnalités Implémentées
🖥️ Interface Utilisateur (Web)
Gestion des Livres : CRUD complet (Ajout, Modification, Suppression, Liste).

Gestion des Lecteurs : Système d'inscription sécurisé avec vérification d'unicité (Nom/Email) et messages d'alerte en cas de doublons.

Système de Réservations :

Réservation de livres disponibles.

Mise à jour automatique du statut du livre (disponible/indisponible).

Annulation de réservation avec libération immédiate du livre.

Recherche & Filtrage : Moteur de recherche par titre/auteur et filtrage par année de publication.

🔌 Interface API (REST Framework)
L'application expose des services web pour une intégration tierce :

GET /api/books/ : Liste tous les livres (supporte le filtre ?year=YYYY).

POST /api/reservations/ : Permet de créer une réservation via un envoi de données JSON.

🛡️ Interface d'Administration (Back-Office)
Le projet utilise l'interface native Django Admin pour une gestion administrative sécurisée :

Authentification & Autorisation : Gestion des utilisateurs (Superusers, Staff) et des droits d'accès.

Gestion de la base de données : Interface intuitive pour superviser les Livres, Lecteurs et Réservations sans passer par le code.

Accès : http://127.0.0.1:8000/admin/

🛠️ Installation et Lancement
Activer l'environnement virtuel :

veuillez taper sur PowerShell
.\venv\Scripts\activate
Installation des dépendances :

veuillez taper sur PowerShell
pip install django djangorestframework
Préparer la base de données :

veuillez taper sur PowerShell
python manage.py migrate
Créer un compte administrateur :

veuillez taper sur PowerShell
python manage.py createsuperuser
Lancer le serveur :

veuillez taper sur PowerShell
python manage.py runserver
Interface Web : http://127.0.0.1:8000/

Interface API : http://127.0.0.1:8000/api/books/

🧪 Tests et Qualité
Tests unitaires : Vérification automatique de la logique métier (notamment l'unicité des réservations).

veuillez taper sur PowerShell
python manage.py test library
Gestion des erreurs : Utilisation de IntegrityError pour sécuriser la base de données et de django.contrib.messages pour informer l'utilisateur en cas d'erreur de saisie (doublons d'emails, etc.).

📂 Structure du Projet
library/ : Application principale (Modèles, Vues, Templates).

library_project/ : Configuration globale et réglages du projet.

serializers.py : Logique de transformation des données pour l'API REST.

✍️ Auteur
Ilboudo Issouf Étudiant en L3S6 - Informatique Université Joseph Ki-Zerbo (U-JKZ).