from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Book, Reservation
from .library.serializers import BookSerializer, ReservationSerializer

@api_view(['GET'])
def api_get_books(request):
    """Récupérer la liste de tous les livres (GET)"""
    books = Book.objects.all()
    serializer = BookSerializer(books, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def api_post_reservation(request):
    """Créer une nouvelle réservation (POST)"""
    serializer = ReservationSerializer(data=request.data)
    if serializer.validate():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)