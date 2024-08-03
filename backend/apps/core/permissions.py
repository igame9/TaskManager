from rest_framework.permissions import BasePermission
import jwt
from settings import settings


class UserWithToken(BasePermission):

    def has_permission(self, request, view):

        token = request.headers.get("Authorization", None)

        if not token:
            return False

        try:
            decoded_token = jwt.decode(jwt=str(token).split("JWT")[1].lstrip(),
                                       key=settings.SIMPLE_JWT['SIGNING_KEY'],
                                       algorithms=[settings.SIMPLE_JWT['ALGORITHM']],
                                       issuer=settings.SIMPLE_JWT["ISSUER"],
                                       audience=settings.SIMPLE_JWT["AUDIENCE"])
            print(decoded_token)

            return True
        except jwt.ExpiredSignatureError as ex:
            print(ex)
            return False
        except jwt.DecodeError as ex:
            print(ex)
            return False
        except jwt.InvalidTokenError as ex:
            print(ex)
            return False
