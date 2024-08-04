from rest_framework.permissions import BasePermission
import jwt
from settings.settings import TOKEN_INFO


class UserWithToken(BasePermission):

    def has_permission(self, request, view):

        header_token = request.headers.get("Authorization", None)

        token = str(header_token).split("JWT")[1].lstrip()

        if not token:
            return False

        try:
            decoded_token = jwt.decode(jwt=token,
                                       key=TOKEN_INFO['SIGNING_KEY'],
                                       algorithms=[TOKEN_INFO['ALGORITHM']],
                                       issuer=TOKEN_INFO["ISSUER"],
                                       audience=TOKEN_INFO["AUDIENCE"])

            request.user_id = decoded_token["user_id"]
            request.email = decoded_token["email"]
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
        except KeyError:
            return False
