from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import AllowAny
from apps.accounts.serializers import UserRegistrationSerializer


class UserRegistrationView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):

        serializer = UserRegistrationSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

        user = serializer.save()

        refresh = RefreshToken.for_user(user)

        tokens = {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }

        return Response({
            'user': serializer.data,
            'tokens': tokens
        }, status=status.HTTP_201_CREATED)

