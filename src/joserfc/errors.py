from typing import Optional


class JoseError(Exception):
    """Base Exception for all errors in joserfc."""

    #: short-string error code
    error: str = ""
    #: long-string to describe this error
    description: str = ""

    def __init__(self, description: Optional[str] = None, error: Optional[str] = None):
        if error is not None:
            self.error = error
        if description is not None:
            self.description = description

        message = "{}: {}".format(self.error, self.description)
        super(JoseError, self).__init__(message)

    def __repr__(self):
        return '<{} "{}">'.format(self.__class__.__name__, self.error)


class DecodeError(JoseError):
    error: str = "decode_error"


class InvalidKeyLengthError(JoseError):
    error: str = "invalid_key_length"


class MissingAlgorithmError(JoseError):
    error: str = "missing_algorithm"
    description: str = 'Missing "alg" value in header'


class MissingEncryptionError(JoseError):
    error: str = "missing_encryption"
    description: str = 'Missing "enc" value in header'


class BadSignatureError(JoseError):
    """This error is designed for JWS/JWT. It is raised when signature
    does not match.
    """
    error: str = "bad_signature"


class InvalidEncryptionAlgorithmError(JoseError):
    """This error is designed for JWE. It is raised when "enc" value
    does not work together with "alg" value.
    """
    error: str = 'invalid_encryption_algorithm'


class UnwrapError(JoseError):
    error: str = "unwrap_error"
    description: str = "Unwrap AES key failed"


class InvalidCEKLengthError(JoseError):
    error: str = "invalid_cek_length"
    description: str = 'Invalid "cek" length'


class InvalidClaimError(JoseError):
    error: str = "invalid_claim"

    def __init__(self, claim):
        description = f'Invalid claim: "{claim}"'
        super(InvalidClaimError, self).__init__(description=description)


class MissingClaimError(JoseError):
    error: str = "missing_claim"

    def __init__(self, claim):
        description = f'Missing claim: "{claim}"'
        super(MissingClaimError, self).__init__(description=description)


class InsecureClaimError(JoseError):
    error: str = "insecure_claim"

    def __init__(self, claim):
        description = f'Insecure claim "{claim}"'
        super(InsecureClaimError, self).__init__(description=description)


class ExpiredTokenError(JoseError):
    error: str = "expired_token"
    description: str = "The token is expired"


class InvalidTokenError(JoseError):
    error: str = "invalid_token"
    description: str = "The token is not valid yet"


class InvalidTypeError(JoseError):
    error: str = "invalid_type"
    description: str = 'The "typ" value in header is invalid'


class InvalidPayloadError(JoseError):
    error: str = "invalid_payload"
