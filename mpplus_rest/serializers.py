from rest_framework import serializers

from .models import Area


class AreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Area
        fields = ('id', 'nome', 'cor', 'icone', 'prioridade')
        # TODO Substituir icon_id por URL do icone
        # TODO Incluir contagem de temas
