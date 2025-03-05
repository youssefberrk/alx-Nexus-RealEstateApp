from django.contrib import admin
from django.contrib.auth import get_user_model

User = get_user_model()

@admin.register(User)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'phone_number', 'role')
    search_fields = ('username', 'email', 'phone_number', 'role')
    list_filter = ('role',)
