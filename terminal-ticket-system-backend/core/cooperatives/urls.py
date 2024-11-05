from django.urls import path
from .views import CoopertivesList, CoopertiveDetail

urlpatterns = [
    path('cooperatives/', CoopertivesList.as_view()),
    path('cooperative/<slug:slug>/', CoopertiveDetail.as_view()),
]