from rest_framework import serializers

from ideas.models import Idea


class IdeaSerializer(serializers.ModelSerializer):
    votes_count = serializers.SerializerMethodField()

    class Meta:
        model = Idea
        fields = ['id', 'company', 'created_by', 'title', 'description', 'status', 'created_at', 'updated_at',
                  'votes_count']
        read_only_fields = ['id', 'company', 'created_by', 'created_at', 'updated_at', 'votes_count']

    def get_votes_count(self, obj):
        return obj.idea_votes.count()
