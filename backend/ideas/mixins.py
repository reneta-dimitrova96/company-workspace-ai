from ideas.models import Idea


class CompanyIdeaQuerysetMixin:
    def get_queryset(self):
        user_ideas = Idea.objects.filter(company=self.request.user.company)
        return user_ideas
