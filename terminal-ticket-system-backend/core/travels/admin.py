from django.contrib import admin
from .seatModel import Seats
from .models import Travels, Cities, Provinces

admin.site.register(Travels)
admin.site.register(Seats)
admin.site.register(Cities)
admin.site.register(Provinces)