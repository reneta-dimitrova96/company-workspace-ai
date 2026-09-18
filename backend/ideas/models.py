from django.db import models
from django.db.models import SET_NULL

from companies.models import Company
from config import settings


class Idea(models.Model):
    class Statuses(models.TextChoices):
        OPEN = "OPEN"
        IN_REVIEW = "IN_REVIEW"
        APPROVED = "APPROVED"
        REJECTED = "REJECTED"

    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=SET_NULL, null=True,
                                   related_name='created_ideas')
    title = models.CharField(max_length=100)
    description = models.TextField()
    status = models.CharField(max_length=12, choices=Statuses.choices, default=Statuses.OPEN)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class IdeaVote(models.Model):
    idea = models.ForeignKey(Idea, on_delete=models.CASCADE, related_name='idea_votes')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user_votes')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Idea votes"
        constraints = [
            models.UniqueConstraint(fields=["idea", "user"], name="idea_and_user_unique_together")
        ]

    def __str__(self):
        return f"{self.user} - {self.idea}"
