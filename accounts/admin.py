# Register your models here.
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DefaultUserAdmin
from django.contrib.admin import ModelAdmin
# Register your models here.

from .models import User


@admin.register(User)
class UserAdmin(DefaultUserAdmin):
    pass
