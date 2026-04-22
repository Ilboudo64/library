# Kata Django - Gestion de Bibliothèque

[cite_start]Ce projet est une application de gestion de bibliothèque permettant de gérer des livres, des lecteurs et des réservations[cite: 3, 5].

## Installation et Lancement
1. **Activer l'environnement virtuel** : `.\venv\Scripts\activate`
2. [cite_start]**Créer la base de données** : `python manage.py migrate` [cite: 35]
3. [cite_start]**Lancer le serveur** : `python manage.py runserver` [cite: 34]

## Tests Unitaires
[cite_start]Pour vérifier la logique métier (notamment l'unicité des réservations)[cite: 27]:
[cite_start]`python manage.py test library` [cite: 36]

## Fonctionnalités implémentées
- [cite_start]CRUD complet pour les Livres et Lecteurs[cite: 11, 14].
- [cite_start]Recherche de livres par titre ou auteur[cite: 12].
- [cite_start]Gestion des réservations avec blocage des doublons[cite: 17, 18].
- [cite_start]Annulation de réservation[cite: 19].