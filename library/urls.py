from django.urls import path
from . import views

urlpatterns = [
    path('', views.book_list, name='book_list'),
    path('readers/', views.reader_list, name='reader_list'),
    path('reservations/', views.reservation_list, name='reservation_list'),
    path('reservations/cancel/<int:res_id>/', views.cancel_reservation, name='cancel_reservation'),
    path('readers/add/', views.add_reader, name='add_reader'),
]