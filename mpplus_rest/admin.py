from django.contrib import admin

from .models import Icone, Area
from .forms import AreaForm


@admin.register(Icone)
class IconeAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['nome']}),
        ('Upload do ícone', {'fields': ['data_file']}),
    ]
    list_display = ('nome', 'updated_at')


@admin.register(Area)
class AreaAdmin(admin.ModelAdmin):
    form = AreaForm
    fieldsets = [
        (None, {
            'fields': ['nome', 'cor', 'icone', 'prioridade']
        }),
    ]
    list_filter = ['updated_at']
    list_display = (
        'id',
        'nome',
        'color_display',
        'icone',
        'prioridade',
        'updated_at'
    )
