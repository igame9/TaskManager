from abc import ABC, abstractmethod
import jwt


class TokenDecoder(ABC):

    @abstractmethod
    def decode_token(self, token: str) -> dict:
        pass


class JWTTokenDecoder(TokenDecoder):
    def __init__(self, signing_key, algorithm, issuer, audience):
        self.signing_key = signing_key
        self.algorithm = algorithm
        self.issuer = issuer
        self.audience = audience

    def decode_token(self, token: str) -> dict:
        try:
            decoded_token = jwt.decode(
                jwt=token,
                key=self.signing_key,
                algorithms=[self.algorithm],
                issuer=self.issuer,
                audience=self.audience
            )
            return decoded_token
        except (jwt.ExpiredSignatureError, jwt.DecodeError, jwt.InvalidTokenError) as ex:
            print(ex)
            return {}


class TokenDecoderFactory:
    @staticmethod
    def create_decoder(token_type: str, token_info: dict) -> TokenDecoder:
        if token_type == "JWT":
            return JWTTokenDecoder(
                signing_key=token_info['SIGNING_KEY'],
                algorithm=token_info['ALGORITHM'],
                issuer=token_info["ISSUER"],
                audience=token_info["AUDIENCE"]
            )
        else:
            raise ValueError(f"Unknown token type: {token_type}")
