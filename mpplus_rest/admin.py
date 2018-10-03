from django.contrib import admin

from .models import Icone


class IconeAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['nome']}),
        ('Upload do ícone', {'fields': ['data_file']}),
    ]
    list_display = ('nome', 'updated_at')


admin.site.register(Icone, IconeAdmin)
