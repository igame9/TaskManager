from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from apps.work_space.serializers import WorkSpaceSerializer
from apps.work_space.models import WorkSpace


class WorkSpaceView(APIView):
    serializer_class = WorkSpaceSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data,
                                           context={"user_uuid": request.user_id})

        if not serializer.is_valid():
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

        serializer.save()

        return Response(status=status.HTTP_201_CREATED)

    def get(self, request):
        user_uuid = request.user_id

        user_work_spaces = WorkSpace.objects.filter(user_uuid=user_uuid)

        serializer = self.serializer_class(user_work_spaces, many=True)

        return Response(serializer.data, status=status.HTTP_201_CREATED)
