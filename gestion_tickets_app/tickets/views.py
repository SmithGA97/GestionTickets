# From DRF
from rest_framework import authentication, permissions, viewsets, mixins
from .serializers import TicketSerializer
from .models import Ticket
# Create your views here.
class TicketListCreateAPIViewset(mixins.ListModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        return Ticket.objects.filter(created_by=self.request.user)