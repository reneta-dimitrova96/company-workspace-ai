from django.shortcuts import get_object_or_404
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated

from tickets.models import Ticket, TicketComment
from tickets.permissions import TicketDetailPermission
from tickets.serializers import TicketSerializer, TicketCommentSerializer


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


class TicketCommentListCreateView(ListCreateAPIView):
    serializer_class = TicketCommentSerializer
    permission_classes = [IsAuthenticated]

    def get_ticket(self):
        return get_object_or_404(
            Ticket,
            pk=self.kwargs.get("ticket_id"),
            company=self.request.user.company,
        )

    def get_queryset(self):
        ticket = self.get_ticket()
        ticket_comments = TicketComment.objects.filter(ticket=ticket)
        return ticket_comments

    def perform_create(self, serializer):
        ticket = self.get_ticket()
        serializer.save(ticket=ticket, author=self.request.user)
