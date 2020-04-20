from django.contrib import admin
from .models import Reservation, AllowReservation
# Register your models here.


@admin.register(Reservation)
class ReservationsAdmin(admin.ModelAdmin):
    list_display = ('cooperative',
                    'datetime',
                    'diners',
                    'status')


@admin.register(AllowReservation)
class AllowReservationsAdmin(admin.ModelAdmin):
    list_display = ('cooperative',
                    'allow_reservation')
