from django.contrib import admin

from .models import Icone, Area, Tema
from .forms import AreaForm


@admin.register(Icone)
class IconeAdmin(admin.ModelAdmin):
    exclude = ('created_at', 'updated_at', )
    list_display = ('nome', 'updated_at')


@admin.register(Area)
class AreaAdmin(admin.ModelAdmin):
    form = AreaForm
    exclude = ('created_at', 'updated_at', )
    list_filter = ['updated_at']
    list_display = (
        'id',
        'nome',
        'color_display',
        'icone',
        'prioridade',
        'updated_at'
    )


@admin.register(Tema)
class TemaAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {'fields': (
            'titulo',
        )}),
        ('Areas', {
            'classes': ('collapse',),
            'fields': (
                'area_mae',
                'areas_correlatas',
            )
        }),
        ('Descrição', {
            'classes': ('collapse',),
            'fields': (
                'subtitulo',
                'descricao',
                'fonte_dados',
                'observacao',
                'prioridade',
            )
        }),
        ('Conexão com dados', {
            'classes': ('collapse',),
            'fields': (
                'tabela_pg',
                'tabela_drive',
                'url_tableau',
            )
        }),
        ('Visibilidade', {
            'classes': ('collapse',),
            'fields': (
                'visivel',
                'dados_craai',
                'dados_estado',
            )
        })
    )
    list_filter = [
        'updated_at',
        'area_mae',
        'visivel',
        'dados_craai',
        'dados_estado',
    ]
    list_display = (
        'id',
        'titulo',
        'area_mae',
        'visivel',
        'updated_at',
    )
