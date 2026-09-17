from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated

from tickets.models import Ticket
from tickets.permissions import TicketDetailPermission
from tickets.serializers import TicketSerializer


class TicketListCreateView(ListCreateAPIView):
    serializer_class = TicketSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        company_tickets = Ticket.objects.filter(company=self.request.user.company)
        return company_tickets

    def perform_create(self, serializer):
        serializer.save(company=self.request.user.company, created_by=self.request.user)


class TicketDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = TicketSerializer
    permission_classes = [IsAuthenticated, TicketDetailPermission]

    def get_queryset(self):
        company_tickets = Ticket.objects.filter(company=self.request.user.company)
        return company_tickets
