from rest_framework.generics import ListAPIView

from companies.serializers import CompanyUserSerializer
from users.models import User
from users.permissions import IsOwnerOrAdmin


class CompanyUsersAPIView(ListAPIView):
    permission_classes = [IsOwnerOrAdmin]
    serializer_class = CompanyUserSerializer

    def get_queryset(self):
        company_users = User.objects.filter(company=self.request.user.company)
        return company_users
