from rest_framework import serializers

from .models import Area, Icone, Tema


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
    count = serializers.SerializerMethodField()

    class Meta:
        model = Area
        depth = 1
        fields = (
            'id',
            'nome',
            'cor',
            'icone',
            'prioridade',
            'count',
        )

    def get_count(self, obj):
        return obj.temas.count() + obj.temas_correlatos.count()


class TemaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tema
        fields = ('id', 'titulo')
