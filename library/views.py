from django.shortcuts import render, redirect,get_object_or_404
from .models import Book, Reader, Reservation
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import BookSerializer, ReservationSerializer
from django.db import IntegrityError
from django.contrib import messages


def book_list(request):
    # 1. Gestion de l'enregistrement (Le formulaire de votre maquette)
    if request.method == "POST":
        title = request.POST.get('title')
        author = request.POST.get('author')
        year = request.POST.get('year')
        if title and author and year:
            Book.objects.create(title=title, author=author, year=year)
            return redirect('book_list') # Recharge la page pour vider le formulaire

    # 2. Gestion de la recherche
    query = request.GET.get('q')
    if query:
        books = Book.objects.filter(title__icontains=query) | Book.objects.filter(author__icontains=query)
    else:
        books = Book.objects.all()

    return render(request, 'library/book_list.html', {'books': books})

def reader_list(request):
    # Si on reçoit des données (bouton Enregistrer cliqué)
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        
        # Création du lecteur dans la base de données
        if name and email:
            Reader.objects.create(name=name, email=email)
            return redirect('reader_list') # Recharge la page pour voir le nouveau lecteur

    # Récupération de tous les lecteurs pour affichage
    readers = Reader.objects.all()
    return render(request, 'library/reader_list.html', {'readers': readers})

def reservation_list(request):
    # On prépare toutes les données nécessaires
    context = {
        'available_books': Book.objects.filter(is_available=True),
        'readers': Reader.objects.all(),
        'active_reservations': Reservation.objects.all().order_by('-date_reservation'),
    }
    
    # On envoie le dictionnaire 'context' au template HTML
    return render(request, 'library/reservation_list.html', context)

def add_reservation(request):
    if request.method == "POST":
        book_id = request.POST.get('book')
        reader_id = request.POST.get('reader')
        
        book = get_object_or_404(Book, id=book_id)
        reader = get_object_or_404(Reader, id=reader_id)

        # Vérification critique
        if not book.is_available:
            messages.error(request, "Ce livre est déjà réservé !")
            return redirect('reservation_list')

        # Créer la réservation et marquer le livre comme indisponible
        Reservation.objects.create(book=book, reader=reader)
        book.is_available = False
        book.save()
        
        return redirect('reservation_list')

def cancel_reservation(request, pk):
    res = get_object_or_404(Reservation, pk=pk)
    book = res.book
    
    # Rendre le livre à nouveau disponible
    book.is_available = True
    book.save()
    
    # Supprimer la réservation
    res.delete()
    return redirect('reservation_list')

def add_reader(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        
        try:
            Reader.objects.create(name=name, email=email)
            messages.success(request, "Lecteur ajouté avec succès !")
        except IntegrityError:
            # C'est ici qu'on gère le message pour l'utilisateur
            messages.error(request, f"Erreur : Le nom '{name}' ou l'email '{email}' est déjà utilisé.")
        
        # Dans tous les cas (succès ou erreur), on revient à la liste
        return redirect('reader_list')
    
    # Si quelqu'un essaie d'accéder à /readers/add/ sans poster de formulaire
    return redirect('reader_list')

# Vue pour modifier
def edit_reader(request, pk):
    reader = get_object_or_404(Reader, pk=pk)
    if request.method == "POST":
        reader.name = request.POST.get('name')
        reader.email = request.POST.get('email')
        reader.save()
        return redirect('reader_list')
    
    # Vous pouvez réutiliser un template spécifique pour l'édition
    return render(request, 'library/edit_reader.html', {'reader': reader})

# Vue pour supprimer
def delete_reader(request, pk):
    reader = get_object_or_404(Reader, pk=pk)
    reader.delete()
    return redirect('reader_list')

from django.shortcuts import render, redirect, get_object_or_404
from .models import Book # Assurez-vous d'importer votre modèle Book

# Vue pour afficher la liste
def book_list(request):
    year_query = request.GET.get('year')
    books = Book.objects.all()

    if year_query:
        books = books.filter(year=year_query) # Filtre strict par année
    
    return render(request, 'library/book_list.html', {'books': books})

# Vue pour AJOUTER (C'est celle qui manque !)
def add_book(request):
    if request.method == "POST":
        title = request.POST.get('title')
        author = request.POST.get('author')
        year = request.POST.get('year')
        Book.objects.create(title=title, author=author, year=year)
        return redirect('book_list')
    return redirect('book_list')

# Vue pour MODIFIER
def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        book.title = request.POST.get('title')
        book.author = request.POST.get('author')
        book.year = request.POST.get('year')
        book.save()
        return redirect('book_list')
    return render(request, 'library/book_list.html') # Ou rediriger selon votre besoin

# Vue pour SUPPRIMER
def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    book.delete()
    return redirect('book_list')

@api_view(['GET'])
def api_get_books(request):
    books = Book.objects.all()
    # Ajout du filtre par année aussi dans l'API
    year = request.GET.get('year')
    if year:
        books = books.filter(year=year)
    serializer = BookSerializer(books, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def api_post_reservation(request):
    serializer = ReservationSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)