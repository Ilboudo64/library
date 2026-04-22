from django.shortcuts import render, redirect,get_object_or_404
from .models import Book, Reader, Reservation


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
    if request.method == "POST":
        book_id = request.POST.get('book_id')
        reader_id = request.POST.get('reader_id')
        
        # Sécurité : vérifier si le livre est toujours disponible [cite: 18]
        book = Book.objects.get(id=book_id)
        if not hasattr(book, 'reservation'):
            reader = Reader.objects.get(id=reader_id)
            Reservation.objects.create(book=book, reader=reader)
        
        return redirect('reservation_list')

    # On ne propose que les livres qui n'ont PAS de réservation [cite: 8]
    available_books = [b for b in Book.objects.all() if not hasattr(b, 'reservation')]
    
    context = {
        'available_books': available_books,
        'readers': Reader.objects.all(),
        'active_reservations': Reservation.objects.all(),
    }
    return render(request, 'library/reservation_list.html', context)

def cancel_reservation(request, res_id):
    reservation = Reservation.objects.get(id=res_id)
    reservation.delete()
    return redirect('reservation_list')

def add_reader(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        
        # Création du lecteur dans la base de données
        Reader.objects.create(name=name, email=email)
        
        # Redirige vers la liste des lecteurs après l'enregistrement
        return redirect('reader_list') # Remplacez par le nom de votre vue de liste
    
    # Si ce n'est pas du POST, on redirige simplement (ou on affiche une erreur)
    return redirect('reader_list')