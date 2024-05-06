from django.utils.dateparse import parse_datetime
from rest_framework import authentication, permissions, viewsets, mixins, serializers
from .serializers import TicketSerializer
from .models import Ticket
# Create your views here.
class TicketListCreateAPIViewset(mixins.ListModelMixin, mixins.CreateModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        queryset =  Ticket.objects.filter(created_by=self.request.user)
        start_date = self.request.query_params.get('start_date')
        end_date = self.request.query_params.get('end_date')
        status = self.request.query_params.get('status')

        if start_date and end_date:
            start_date_p = parse_datetime(start_date)
            end_date_p = parse_datetime(end_date)
            if start_date_p and end_date_p:
                queryset = queryset.filter(creation_date__range=(start_date, end_date))
            else:
                raise serializers.ValidationError('Invalid datetime format provided: start_date and end_date  must be something like YYYY-MM-DDTHH:MM:SS, ex: 2024-05-05T15:35:00')

        if status and status in ('NOT_STARTED', 'IN_PROCESS', 'COMPLETED'):
            queryset = queryset.filter(status=status)
        elif status and status not in ('NOT_STARTED', 'IN_PROCESS', 'COMPLETED'):
            raise serializers.ValidationError("Status must be 'NOT_STARTED, IN_PROCESS, or COMPLETED")
        return queryset
