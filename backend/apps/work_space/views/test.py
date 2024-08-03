from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated


class TestView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        answer = {
            "message": "Вы вошли в микросервис"
        }

        return Response(answer, status=status.HTTP_201_CREATED)
