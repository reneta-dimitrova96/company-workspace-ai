from django.db.models import Count, Q
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from ideas.models import Idea
from tickets.models import Ticket
from users.models import User


class DashboardView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        company = request.user.company
        ticket_stats = Ticket.objects.filter(company=company).aggregate(
            total=Count("id"),
            open=Count("id", filter=Q(status=Ticket.Statuses.OPEN)),
            in_progress=Count("id", filter=Q(status=Ticket.Statuses.IN_PROGRESS)),
            done=Count("id", filter=Q(status=Ticket.Statuses.DONE)),
        )

        idea_stats = Idea.objects.filter(company=company).aggregate(
            total=Count("id"),
            open=Count("id", filter=Q(status=Idea.Statuses.OPEN)),
            in_review=Count("id", filter=Q(status=Idea.Statuses.IN_REVIEW)),
            approved=Count("id", filter=Q(status=Idea.Statuses.APPROVED)),
            rejected=Count("id", filter=Q(status=Idea.Statuses.REJECTED)),
        )

        users_count = User.objects.filter(company=company).count()
        return Response({
            "tickets": ticket_stats,
            "ideas": idea_stats,
            "users": {
                "total": users_count
            }
        })
