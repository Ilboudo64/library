from django.test import TestCase
from .models import Book, Reader, Reservation
from django.db import IntegrityError

class ReservationTest(TestCase):
    def setUp(self):
        self.book = Book.objects.create(title="Django Pro", author="Expert", year=2024)
        self.reader1 = Reader.objects.create(name="Arnaud", email="arnaud@test.com")
        self.reader2 = Reader.objects.create(name="Ivan", email="ivan@test.com")

    def test_unique_reservation_per_book(self):
        """Vérifie qu'un livre ne peut pas être réservé deux fois [cite: 8]"""
        # Première réservation
        Reservation.objects.create(book=self.book, reader=self.reader1)
        
        # Tentative de deuxième réservation sur le même livre
        with self.assertRaises(IntegrityError):
            Reservation.objects.create(book=self.book, reader=self.reader2)