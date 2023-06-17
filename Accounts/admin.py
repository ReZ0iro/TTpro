from django.contrib import admin
from .models import UserAccounts 
from django.contrib.auth.admin import UserAdmin
# Register your models here.

class AdminUserAccounts(UserAdmin) : 
    list_display = ("id" , "username", "is_active","is_verified","user_role",)
    filter_horizontal = ("following",)
    list_filter = ("following",)
    fieldsets = ()

admin.site.register(UserAccounts , AdminUserAccounts)