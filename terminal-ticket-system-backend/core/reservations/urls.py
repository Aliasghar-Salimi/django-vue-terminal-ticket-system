from django.urls import path, re_path
from .views import ReservationsList, ReservationDetail

urlpatterns = [
    path('reservations/', ReservationsList.as_view()),
    re_path('reservation/(?P<slug>[-\w]+)/', ReservationDetail.as_view())
]