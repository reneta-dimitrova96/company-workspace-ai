from rest_framework import serializers

from tickets.models import Ticket, TicketComment


class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = (
            "id",
            "company",
            "created_by",
            "assigned_to",
            "title",
            "description",
            "status",
            "priority",
            "created_at",
            "updated_at",
        )
        read_only_fields = ('id', 'company', 'created_by', 'created_at', 'updated_at')

    def validate_assigned_to(self, assigned_user):
        if assigned_user is None:
            return None

        current_user = self.context["request"].user

        if assigned_user.company != current_user.company:
            raise serializers.ValidationError(
                "Assigned user must belong to the same company."
            )

        return assigned_user


class TicketCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = TicketComment
        fields = ['id', 'ticket', 'author', 'content', 'created_at']
        read_only_fields = ('id', 'ticket', 'author', 'created_at')
