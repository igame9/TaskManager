from rest_framework import serializers
from apps.work_space.models import WorkSpace
from rest_framework.serializers import ValidationError


class WorkSpaceSerializer(serializers.ModelSerializer):
    user_uuid = serializers.UUIDField(required=True)
    name = serializers.CharField(required=True)
    created_at = serializers.DateTimeField(required=False)

    class Meta:
        model = WorkSpace
        fields = [
            'user_uuid',
            'name',
            'created_at',
        ]

    def validate(self, data):

        user_uuid_token = self.context["user_uuid"]
        user_uuid_request = data["user_uuid"]

        if str(user_uuid_token) != str(user_uuid_request):
            raise ValidationError("Invalid uuid")

        return data

    def create(self, validated_data):
        user_uuid = validated_data["user_uuid"]
        work_space_name = validated_data["name"]

        try:
            work_space = WorkSpace.objects.get(user_uuid=user_uuid,
                                               name=work_space_name)
        except WorkSpace.DoesNotExist:
            work_space = WorkSpace(user_uuid=user_uuid)

        work_space.name = work_space_name
        work_space.save()
        return work_space
