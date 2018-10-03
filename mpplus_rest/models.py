from django.db import models


class Icones(models.Model):
    nome = models.CharField(max_length=255)
    data_file = models.FileField(upload_to='icons/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Areas(models.Model):
    nome = models.CharField(max_length=255)
    cor = models.CharField(max_length=7)
    icone = models.ForeignKey(
        Icones,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    prioridade = models.IntegerField(),
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
