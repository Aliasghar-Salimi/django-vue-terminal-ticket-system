from django.urls import path, re_path
from .views import CoopertivesList, CoopertiveDetail

urlpatterns = [
    path('cooperatives/', CoopertivesList.as_view()),
    re_path('cooperative/(?P<slug>[-\w]+)/', CoopertiveDetail.as_view()),
]