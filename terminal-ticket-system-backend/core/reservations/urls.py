from django.urls import path
from .views import ReservationsList, ReservationDetail

urlpatterns = [
    path('reservations/', ReservationsList.as_view()),
    path('reservation/<slug:slug>', ReservationDetail.as_view())
]