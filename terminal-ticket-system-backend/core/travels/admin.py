from django.contrib import admin
from .seatModel import Seats
from .models import Travels

admin.site.register(Travels)
admin.site.register(Seats)