from django.contrib import admin

from habbit.models import Habbit


@admin.register(Habbit)
class HabitAdmin(admin.ModelAdmin):
    """Класс для отображения атрибутов в панели админки"""
    list_display = ('id', 'action')
