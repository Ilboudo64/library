📚 Gestion de Bibliothèque - Django Kata
Ce projet est une application complète de gestion de bibliothèque développée avec Django 6.0. Elle permet de gérer le cycle de vie des livres, des lecteurs et des réservations, tout en offrant une interface de programmation (API) pour des extensions futures (mobile/web).

🚀 Fonctionnalités Implémentées
🖥️ Interface Utilisateur (Web)
Gestion des Livres : CRUD complet (Ajout, Modification, Suppression, Liste).

Gestion des Lecteurs : Système d'inscription sécurisé avec vérification d'unicité (Nom/Email) et messages d'alerte.

Système de Réservations :

Réservation de livres disponibles.

Mise à jour automatique du statut du livre (disponible/indisponible).

Annulation de réservation avec libération du livre.

Recherche & Filtrage : Recherche par titre/auteur et filtrage par année de publication.

🔌 interface API (REST Framework)
Endpoints API :

GET /api/books/ : Liste tous les livres (supporte le filtre ?year=YYYY).

POST /api/reservations/ : Permet de créer une réservation via JSON.

🛠️ Installation et Lancement
Environnement virtuel :

PowerShell
.\venv\Scripts\activate
Installation des dépendances :
(Vérifiez d'avoir installé Django et d'importantes bibliothèques comme djangorestframework)

sur PowerShell veuillez taper
pip install django djangorestframework
Base de données :

sur PowerShell veuillez taper
python manage.py migrate
Lancement :

sur PowerShell veuillez taper
python manage.py runserver
Accès à l'interface : http://127.0.0.1:8000/
Accès à l'API : http://127.0.0.1:8000/api/books/

🧪 Tests et Qualité
Tests unitaires : Vérification de la logique métier (réservations, modèles).

PowerShell
python manage.py test library
Gestion des erreurs : Implémentation de IntegrityError pour empêcher les doublons de lecteurs et affichage de messages "User-Friendly" via django.contrib.messages.

📂 Structure du Projet
library/ : Application principale (Modèles, Vues, Templates).

library_project/ : Configuration globale du projet.

serializers.py : Transformation des données pour l'API REST.

✍️ Auteur
Ilboudo Issouf Étudiant en L3S6 - Informatique, Université Joseph Ki-Zerbo.
