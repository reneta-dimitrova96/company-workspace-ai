from django.db.models import Count

from ideas.models import Idea


class CompanyIdeaQuerysetMixin:
    def get_queryset(self):
        user_ideas = (
            Idea.objects
            .filter(company=self.request.user.company)
            .annotate(votes_count=Count("idea_votes"))
        )

        return user_ideas
