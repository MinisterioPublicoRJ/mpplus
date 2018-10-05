from rest_framework import serializers

from .models import Area, Icone


class IconeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Icone
        fields = ('data_file', )

    def to_representation(self, value):
        request = self.context.get('request')
        return request.build_absolute_uri(
            value.data_file.url
        )


class AreaSerializer(serializers.ModelSerializer):
    icone = IconeSerializer()

    class Meta:
        model = Area
        depth = 1
        fields = ('id', 'nome', 'cor', 'prioridade', 'icone')
        # TODO Incluir contagem de temas
