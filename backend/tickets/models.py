from django.db import models
from django.db.models import SET_NULL, CASCADE

from companies.models import Company
from config import settings


class Ticket(models.Model):
    class Statuses(models.TextChoices):
        OPEN = "OPEN"
        IN_PROGRESS = "IN_PROGRESS"
        DONE = "DONE"

    class Priorities(models.TextChoices):
        LOW = "LOW"
        MEDIUM = "MEDIUM"
        HIGH = "HIGH"

    company = models.ForeignKey(Company, on_delete=CASCADE)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=SET_NULL, null=True,
                                   related_name='created_tickets')
    assigned_to = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=SET_NULL, blank=True, null=True,
                                    related_name='assigned_tickets')
    title = models.CharField(max_length=100)
    description = models.TextField()
    status = models.CharField(max_length=12, choices=Statuses.choices, default=Statuses.OPEN)
    priority = models.CharField(max_length=10, choices=Priorities.choices, default=Priorities.MEDIUM)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class TicketComment(models.Model):
    ticket = models.ForeignKey(Ticket, on_delete=CASCADE, related_name='ticket_comments')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=SET_NULL, null=True, related_name='user_comments')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.ticket.title + ' ' + (self.author.username if self.author else 'Unknown user')
