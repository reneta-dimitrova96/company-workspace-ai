from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from users.serializers import RegisterUserSerializer


class RegisterUserView(APIView):
    permission_classes = [AllowAny]
    serializer_class = RegisterUserSerializer

    def post(self, request):
        user_serializer = self.serializer_class(data=request.data)
        user_serializer.is_valid(raise_exception=True)
        user = user_serializer.save()

        return Response(data={'created_user_id': user.id}, status=status.HTTP_201_CREATED)
