from django.db import models
from django.utils.html import format_html
from colorfield.fields import ColorField


class Icone(models.Model):
    nome = models.CharField(max_length=255)
    data_file = models.FileField(upload_to='icons/')
    file_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome


class Area(models.Model):
    nome = models.CharField(max_length=255)
    cor = ColorField(default='#FF0000')
    icone = models.ForeignKey(
        Icone,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    prioridade = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

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
