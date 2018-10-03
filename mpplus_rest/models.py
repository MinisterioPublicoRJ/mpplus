from django.db.models import (
    Model,
    CharField,
    DateTimeField,
    FileField,
    ForeignKey,
    IntegerField,
    SET_NULL,
)
from django.utils.html import format_html
from colorfield.fields import ColorField


class Icone(Model):
    nome = CharField(max_length=255)
    data_file = FileField(upload_to='icons/')
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome


class Area(Model):
    nome = CharField(max_length=255)
    cor = ColorField(default='#FF0000')
    icone = ForeignKey(
        Icone,
        on_delete=SET_NULL,
        blank=True,
        null=True,
    )
    prioridade = IntegerField(default=1)
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome

    def color_display(self):
        return format_html(
            '<span class="color-box" style="background-color: {};">\
            </span>\
            {}',
            self.cor,
            self.cor,
        )
