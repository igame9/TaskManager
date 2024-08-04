from rest_framework.permissions import BasePermission
from apps.core.services import TokenDecoderFactory
from settings.settings import TOKEN_INFO, TOKEN_HEADER_PREFIX


class UserWithToken(BasePermission):

    def has_permission(self, request, view):
        header_token = request.headers.get("Authorization", None)

        token = str(header_token).split(f"{TOKEN_HEADER_PREFIX}")[1].lstrip()

        if not token:
            return False

        token_decoder = TokenDecoderFactory.create_decoder(token_type=TOKEN_HEADER_PREFIX,
                                                           token_info=TOKEN_INFO)

        decoded_token = token_decoder.decode_token(token)

        if decoded_token:
            request.user_id = decoded_token["user_id"]
            request.email = decoded_token["email"]
            return True

        return False
