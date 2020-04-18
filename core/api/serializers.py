from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer
from core.models import PontoTuristico
from atracoes.api.serializers import AtracaoSerializer
from enderecos.api.serializers import EnderecoSerializer


class PontoTuristicoSerializer(ModelSerializer):
    atracoes = AtracaoSerializer(many=True, read_only=True)
    endereco = EnderecoSerializer(read_only=True)
    descricao_completa = SerializerMethodField()

    class Meta:
        model = PontoTuristico
        fields = ('id', 'nome', 'descricao', 'aprovado', 'foto',
                  'atracoes', 'comentarios', 'avaliacao', 'endereco',
                  'descricao_completa', 'descricao_completa2', )
        read_only_fields = ('comentarios', 'avaliacoes')

    def creat(self, validadted_data):
        atracoes = validadted_data['atracoes']

    def get_descricao_completa(self, obj):
        return '%s - %s' % (obj.nome, obj.descricao)
