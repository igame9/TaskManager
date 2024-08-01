from apps.accounts.models import ApplicationUser
from rest_framework import serializers


class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = ApplicationUser
        fields = ['password',
                  'email']

    def create(self, validated_data):
        print(validated_data)
        user = ApplicationUser.objects.create_user(
            password=validated_data['password'],
            email=validated_data['email']
        )
        return user
