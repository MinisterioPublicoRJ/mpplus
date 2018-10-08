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
        fields = (
            'id',
            'nome',
            'cor',
            'icone',
            'prioridade',
            'count',
        )

    def get_count(self, obj):
        return obj.temas.filter(visivel=True).count() +\
               obj.temas_correlatos.filter(visivel=True).count()


class InternalAreaSerializer(serializers.ModelSerializer):
    icone = IconeSerializer()

    class Meta:
        model = Area
        fields = (
            'id',
            'nome',
            'cor',
            'icone',
        )


class TemaSerializer(serializers.ModelSerializer):
    data_criacao = serializers.DateTimeField(
        source='created_at',
        format='%d/%m/%Y'
    )
    endpoint = serializers.SerializerMethodField()
    area_mae = InternalAreaSerializer()
    areas_correlatas = serializers.PrimaryKeyRelatedField(
        many=True,
        read_only=True
    )
    fonte = serializers.CharField(
        source='fonte_dados',
        allow_blank=True
    )
    url = serializers.URLField(
        source='url_tableau',
        allow_blank=True
    )

    class Meta:
        model = Tema
        depth = 1
        fields = (
            'id',
            'data_criacao',
            'titulo',
            'endpoint',
            'area_mae',
            'areas_correlatas',
            'subtitulo',
            'descricao',
            'fonte',
            'observacao',
            'url',
            'prioridade',
        )

    def get_endpoint(self, obj):
        return obj.titulo.replace(' ', '')
