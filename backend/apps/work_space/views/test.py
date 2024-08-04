from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class TestView(APIView):

    def post(self, request):
        # print(request.email)
        # print(request.user_id)
        answer = {
            "message": "Вы вошли в микросервис"
        }

        return Response(answer, status=status.HTTP_200_OK)
