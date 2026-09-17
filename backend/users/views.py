from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from users.serializers import RegisterUserSerializer, CurrentUserSerializer


class RegisterUserView(APIView):
    permission_classes = [AllowAny]
    serializer_class = RegisterUserSerializer

    def post(self, request):
        user_serializer = self.serializer_class(data=request.data)
        user_serializer.is_valid(raise_exception=True)
        user = user_serializer.save()

        return Response(data={'created_user_id': user.id}, status=status.HTTP_201_CREATED)


class CurrentUserView(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = CurrentUserSerializer

    def get(self, request):
        current_user = request.user
        serializer = self.serializer_class(current_user)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
