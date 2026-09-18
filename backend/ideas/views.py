from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from ideas.models import Idea, IdeaVote
from ideas.serializers import IdeaSerializer


class IdeaListCreateView(ListCreateAPIView):
    serializer_class = IdeaSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user_ideas = Idea.objects.filter(company=self.request.user.company)
        return user_ideas

    def perform_create(self, serializer):
        serializer.save(company=self.request.user.company, created_by=self.request.user)


class IdeaVoteView(APIView):
    permission_classes = [IsAuthenticated]

    def get_idea(self, idea_id):
        return get_object_or_404(
            Idea,
            pk=idea_id,
            company=self.request.user.company,
        )

    def post(self, request, idea_id):
        idea = self.get_idea(idea_id)
        vote, is_created = IdeaVote.objects.get_or_create(idea=idea, user=request.user)
        if is_created:
            return Response(
                data={
                    "vote_id": vote.id,
                    "created": True,
                },
                status=status.HTTP_201_CREATED,
            )

        return Response(
            data={
                "vote_id": vote.id,
                "created": False,
            },
            status=status.HTTP_200_OK,
        )

    def delete(self, request, idea_id):
        idea = self.get_idea(idea_id)
        deleted_count, _ = IdeaVote.objects.filter(
            idea=idea,
            user=request.user,
        ).delete()
        if deleted_count == 0:
            return Response(
                status=status.HTTP_404_NOT_FOUND,
            )

        return Response(
            status=status.HTTP_204_NO_CONTENT,
        )
