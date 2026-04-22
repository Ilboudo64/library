from django.contrib import admin
from django.urls import path, include
from library import views  # Import correct depuis l'application 'library'

# Supprime les lignes "from . import views" si elles existent encore

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Routes principales
    path('', views.book_list, name='book_list'),
    path('readers/', views.reader_list, name='reader_list'),
    path('readers/add/', views.add_reader, name='add_reader'),
    path('readers/edit/<int:pk>/', views.edit_reader, name='edit_reader'),
    path('readers/delete/<int:pk>/', views.delete_reader, name='delete_reader'),
    
    # Routes Catalogue
    path('catalogue/add/', views.add_book, name='add_book'),
    path('catalogue/edit/<int:pk>/', views.edit_book, name='edit_book'),
    path('catalogue/delete/<int:pk>/', views.delete_book, name='delete_book'),
    
    # Routes Réservations
    path('reservations/', views.reservation_list, name='reservation_list'),
    path('reservations/add/', views.add_reservation, name='add_reservation'),
    path('reservations/cancel/<int:pk>/', views.cancel_reservation, name='cancel_reservation'),

    # Routes API (Assure-toi que ces fonctions existent dans ton library/views.py)
    path('api/books/', views.api_get_books, name='api_books'),
    path('api/reservations/', views.api_post_reservation, name='api_reservation'),
]