from rest_framework import viewsets
from electronics.permissions import IsActive
from electronics.models import Network
from electronics.serializers import NetworkSerializers
from rest_framework.filters import OrderingFilter


class NetworkViewSet(viewsets.ModelViewSet):
    serializer_class = NetworkSerializers
    queryset = Network.objects.all()
    permission_classes = [IsActive]
    filter_backends = [
        OrderingFilter,
    ]
    ordering_fields = [
        "contacts__city",
    ]
