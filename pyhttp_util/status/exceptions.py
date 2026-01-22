"""HTTP status code exception hierarchy."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from pyhttp_util.status.status_enum import HTTPStatus

__all__ = (
    # Base exceptions
    "HTTPStatusError",
    "InformationalResponse",
    "RedirectResponse",
    "ClientError",
    "ServerError",
    # 4xx Client errors
    "BadRequestError",
    "UnauthorizedError",
    "PaymentRequiredError",
    "ForbiddenError",
    "NotFoundError",
    "MethodNotAllowedError",
    "NotAcceptableError",
    "ProxyAuthenticationRequiredError",
    "RequestTimeoutError",
    "ConflictError",
    "GoneError",
    "LengthRequiredError",
    "PreconditionFailedError",
    "ContentTooLargeError",
    "URITooLongError",
    "UnsupportedMediaTypeError",
    "RangeNotSatisfiableError",
    "ExpectationFailedError",
    "ImATeapotError",
    "MisdirectedRequestError",
    "UnprocessableEntityError",
    "LockedError",
    "FailedDependencyError",
    "TooEarlyError",
    "UpgradeRequiredError",
    "PreconditionRequiredError",
    "TooManyRequestsError",
    "RequestHeaderFieldsTooLargeError",
    "UnavailableForLegalReasonsError",
    # 5xx Server errors
    "InternalServerError",
    "NotImplementedError_",
    "BadGatewayError",
    "ServiceUnavailableError",
    "GatewayTimeoutError",
    "HTTPVersionNotSupportedError",
    "VariantAlsoNegotiatesError",
    "InsufficientStorageError",
    "LoopDetectedError",
    "NotExtendedError",
    "NetworkAuthenticationRequiredError",
)


class HTTPStatusError(Exception):
    """Base exception for HTTP status code errors.

    Attributes:
        status_code: The HTTP status code associated with this error.
        message: The error message.
    """

    status_code: int | HTTPStatus | None = None
    default_message: str = "HTTP error occurred"

    def __init__(
        self,
        message: str | None = None,
        status_code: int | HTTPStatus | None = None,
    ) -> None:
        self.message = message or self.default_message
        if status_code is not None:
            self.status_code = status_code
        super().__init__(self.message)


# Category base exceptions


class InformationalResponse(HTTPStatusError):
    """Base exception for 1xx informational responses."""

    default_message = "Informational response"


class RedirectResponse(HTTPStatusError):
    """Base exception for 3xx redirect responses."""

    default_message = "Redirect response"


class ClientError(HTTPStatusError):
    """Base exception for 4xx client errors."""

    default_message = "Client error"


class ServerError(HTTPStatusError):
    """Base exception for 5xx server errors."""

    default_message = "Server error"


# 4xx Client Error Exceptions


class BadRequestError(ClientError):
    """400 Bad Request."""

    status_code = 400
    default_message = "Bad Request"


class UnauthorizedError(ClientError):
    """401 Unauthorized."""

    status_code = 401
    default_message = "Unauthorized"


class PaymentRequiredError(ClientError):
    """402 Payment Required."""

    status_code = 402
    default_message = "Payment Required"


class ForbiddenError(ClientError):
    """403 Forbidden."""

    status_code = 403
    default_message = "Forbidden"


class NotFoundError(ClientError):
    """404 Not Found."""

    status_code = 404
    default_message = "Not Found"


class MethodNotAllowedError(ClientError):
    """405 Method Not Allowed."""

    status_code = 405
    default_message = "Method Not Allowed"


class NotAcceptableError(ClientError):
    """406 Not Acceptable."""

    status_code = 406
    default_message = "Not Acceptable"


class ProxyAuthenticationRequiredError(ClientError):
    """407 Proxy Authentication Required."""

    status_code = 407
    default_message = "Proxy Authentication Required"


class RequestTimeoutError(ClientError):
    """408 Request Timeout."""

    status_code = 408
    default_message = "Request Timeout"


class ConflictError(ClientError):
    """409 Conflict."""

    status_code = 409
    default_message = "Conflict"


class GoneError(ClientError):
    """410 Gone."""

    status_code = 410
    default_message = "Gone"


class LengthRequiredError(ClientError):
    """411 Length Required."""

    status_code = 411
    default_message = "Length Required"


class PreconditionFailedError(ClientError):
    """412 Precondition Failed."""

    status_code = 412
    default_message = "Precondition Failed"


class ContentTooLargeError(ClientError):
    """413 Content Too Large."""

    status_code = 413
    default_message = "Content Too Large"


class URITooLongError(ClientError):
    """414 URI Too Long."""

    status_code = 414
    default_message = "URI Too Long"


class UnsupportedMediaTypeError(ClientError):
    """415 Unsupported Media Type."""

    status_code = 415
    default_message = "Unsupported Media Type"


class RangeNotSatisfiableError(ClientError):
    """416 Range Not Satisfiable."""

    status_code = 416
    default_message = "Range Not Satisfiable"


class ExpectationFailedError(ClientError):
    """417 Expectation Failed."""

    status_code = 417
    default_message = "Expectation Failed"


class ImATeapotError(ClientError):
    """418 I'm a Teapot."""

    status_code = 418
    default_message = "I'm a Teapot"


class MisdirectedRequestError(ClientError):
    """421 Misdirected Request."""

    status_code = 421
    default_message = "Misdirected Request"


class UnprocessableEntityError(ClientError):
    """422 Unprocessable Entity."""

    status_code = 422
    default_message = "Unprocessable Entity"


class LockedError(ClientError):
    """423 Locked."""

    status_code = 423
    default_message = "Locked"


class FailedDependencyError(ClientError):
    """424 Failed Dependency."""

    status_code = 424
    default_message = "Failed Dependency"


class TooEarlyError(ClientError):
    """425 Too Early."""

    status_code = 425
    default_message = "Too Early"


class UpgradeRequiredError(ClientError):
    """426 Upgrade Required."""

    status_code = 426
    default_message = "Upgrade Required"


class PreconditionRequiredError(ClientError):
    """428 Precondition Required."""

    status_code = 428
    default_message = "Precondition Required"


class TooManyRequestsError(ClientError):
    """429 Too Many Requests."""

    status_code = 429
    default_message = "Too Many Requests"


class RequestHeaderFieldsTooLargeError(ClientError):
    """431 Request Header Fields Too Large."""

    status_code = 431
    default_message = "Request Header Fields Too Large"


class UnavailableForLegalReasonsError(ClientError):
    """451 Unavailable For Legal Reasons."""

    status_code = 451
    default_message = "Unavailable For Legal Reasons"


# 5xx Server Error Exceptions


class InternalServerError(ServerError):
    """500 Internal Server Error."""

    status_code = 500
    default_message = "Internal Server Error"


class NotImplementedError_(ServerError):
    """501 Not Implemented.

    Note: Named with trailing underscore to avoid conflict with
    the built-in NotImplementedError.
    """

    status_code = 501
    default_message = "Not Implemented"


class BadGatewayError(ServerError):
    """502 Bad Gateway."""

    status_code = 502
    default_message = "Bad Gateway"


class ServiceUnavailableError(ServerError):
    """503 Service Unavailable."""

    status_code = 503
    default_message = "Service Unavailable"


class GatewayTimeoutError(ServerError):
    """504 Gateway Timeout."""

    status_code = 504
    default_message = "Gateway Timeout"


class HTTPVersionNotSupportedError(ServerError):
    """505 HTTP Version Not Supported."""

    status_code = 505
    default_message = "HTTP Version Not Supported"


class VariantAlsoNegotiatesError(ServerError):
    """506 Variant Also Negotiates."""

    status_code = 506
    default_message = "Variant Also Negotiates"


class InsufficientStorageError(ServerError):
    """507 Insufficient Storage."""

    status_code = 507
    default_message = "Insufficient Storage"


class LoopDetectedError(ServerError):
    """508 Loop Detected."""

    status_code = 508
    default_message = "Loop Detected"


class NotExtendedError(ServerError):
    """510 Not Extended."""

    status_code = 510
    default_message = "Not Extended"


class NetworkAuthenticationRequiredError(ServerError):
    """511 Network Authentication Required."""

    status_code = 511
    default_message = "Network Authentication Required"


# Mapping from status codes to exception classes
_STATUS_CODE_TO_EXCEPTION: dict[int, type[HTTPStatusError]] = {
    400: BadRequestError,
    401: UnauthorizedError,
    402: PaymentRequiredError,
    403: ForbiddenError,
    404: NotFoundError,
    405: MethodNotAllowedError,
    406: NotAcceptableError,
    407: ProxyAuthenticationRequiredError,
    408: RequestTimeoutError,
    409: ConflictError,
    410: GoneError,
    411: LengthRequiredError,
    412: PreconditionFailedError,
    413: ContentTooLargeError,
    414: URITooLongError,
    415: UnsupportedMediaTypeError,
    416: RangeNotSatisfiableError,
    417: ExpectationFailedError,
    418: ImATeapotError,
    421: MisdirectedRequestError,
    422: UnprocessableEntityError,
    423: LockedError,
    424: FailedDependencyError,
    425: TooEarlyError,
    426: UpgradeRequiredError,
    428: PreconditionRequiredError,
    429: TooManyRequestsError,
    431: RequestHeaderFieldsTooLargeError,
    451: UnavailableForLegalReasonsError,
    500: InternalServerError,
    501: NotImplementedError_,
    502: BadGatewayError,
    503: ServiceUnavailableError,
    504: GatewayTimeoutError,
    505: HTTPVersionNotSupportedError,
    506: VariantAlsoNegotiatesError,
    507: InsufficientStorageError,
    508: LoopDetectedError,
    510: NotExtendedError,
    511: NetworkAuthenticationRequiredError,
}


def get_exception_for_status(code: int) -> type[HTTPStatusError]:
    """Get the appropriate exception class for a status code.

    Args:
        code: The HTTP status code.

    Returns:
        The exception class for the status code, or a base category
        exception if no specific exception exists.
    """
    if code in _STATUS_CODE_TO_EXCEPTION:
        return _STATUS_CODE_TO_EXCEPTION[code]

    if 100 <= code < 200:
        return InformationalResponse
    if 300 <= code < 400:
        return RedirectResponse
    if 400 <= code < 500:
        return ClientError
    if 500 <= code < 600:
        return ServerError

    return HTTPStatusError
