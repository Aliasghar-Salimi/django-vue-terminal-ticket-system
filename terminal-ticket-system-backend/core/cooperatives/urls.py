from django.urls import path
from .views import CoopertivesList, CoopertiveDetail

urlpatterns = [
    path('coopertives/', CoopertivesList.as_view()),
    path('coopertive/<slug:slug>/', CoopertiveDetail.as_view()),
]