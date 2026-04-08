from django.contrib import admin

from users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """Класс для отображения атрибутов в панели админки"""
    list_display = ('id', 'email',)
