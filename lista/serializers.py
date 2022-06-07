from rest_framework import serializers
from .models import tabela_cliente

class ClientesSerializers(serializers.ModelSerializer):
    
    class Meta:
        id = serializers.PrimaryKeyRelatedField(many=False, read_only=True)
        client_name = serializers.CharField()
        email = serializers.EmailField()

        model = tabela_cliente
        fields = '__all__'
        
        def create(self, validated_data):
            return tabela_cliente.objects.create(**validated_data)

        def update(self, validated_data):
            clientes = tabela_cliente(**validated_data)
            clientes.save()
            return clientes
