from django.contrib import admin
from cooperatives.models import Cooperative, Category, Timetable


@admin.register(Category)
class CategoruAdmin(admin.ModelAdmin):
    list_display = ('name',
                    'name_pretty',
                    )


@admin.register(Cooperative)
class CooperativeAdmin(admin.ModelAdmin):
    list_display = ('name',
                    'short_description',
                    'logo',
                    'description',
                    'phone',
                    'facebook',
                    'address',
                    'map_latitude',
                    'map_longitude',
                    'whatsapp',
                    )


@admin.register(Timetable)
class TimetableAdmin(admin.ModelAdmin):
    list_display = ('cooperative',
                    'monday_open',
                    'monday_close',
                    'tuesday_open',
                    'tuesday_close',
                    'wednesday_open',
                    'wednesday_close',
                    'thursday_open',
                    'thursday_close',
                    'friday_open',
                    'friday_close',
                    'saturday_open',
                    'saturday_close',
                    'sunday_open',
                    'sunday_close'
                    )
