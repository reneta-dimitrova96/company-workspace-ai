from django.contrib.auth.password_validation import validate_password
from django.db import transaction
from rest_framework import serializers

from companies.models import Company
from users.models import User


class RegisterUserSerializer(serializers.ModelSerializer):
    company_name = serializers.CharField(max_length=100, write_only=True)
    password = serializers.CharField(
        write_only=True,
        validators=[validate_password],
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'company_name']

    @transaction.atomic
    def create(self, validated_data):
        company_name = validated_data.pop('company_name')
        company = Company.objects.create(name=company_name)

        user = User.objects.create_user(
            role=User.Roles.OWNER,
            company=company,
            **validated_data)

        return user


class CurrentUserSerializer(serializers.ModelSerializer):
    company = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'role', 'company']
        read_only_fields = ['id', 'username', 'email', 'role', 'company']

    def get_company(self, obj):
        return obj.company.name if obj.company else None
