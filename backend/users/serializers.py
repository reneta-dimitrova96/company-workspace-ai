from django.db import transaction
from rest_framework import serializers

from companies.models import Company
from users.models import User


class RegisterUserSerializer(serializers.ModelSerializer):
    company_name = serializers.CharField(max_length=100)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'company_name']
        extra_kwargs = {'password': {'write_only': True}}

    @transaction.atomic
    def create(self, validated_data):
        company_name = validated_data.pop('company_name')
        company = Company.objects.create(name=company_name)

        user = User.objects.create_user(
            role=User.Roles.OWNER,
            company=company,
            **validated_data)

        return user
