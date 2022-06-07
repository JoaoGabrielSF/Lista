from .models import tabela_cliente
from .serializers import ClientesSerializers
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

# Create your views here.


class ClientesViewSet(viewsets.ModelViewSet):

    permission_classes = (IsAuthenticated, )
    queryset = tabela_cliente.objects.all()
    serializer_class = ClientesSerializers

