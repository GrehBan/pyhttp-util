"""HTTP status codes enumeration with phrases and descriptions."""

from __future__ import annotations

from enum import Enum

__all__ = ("HTTPStatus",)


class HTTPStatus(int, Enum):
    """Enumeration of HTTP status codes.

    Each member has an integer value (the status code) and provides
    properties for the phrase and description. Inherits from int,
    so can be used directly in comparisons with integers.

    Attributes:
        phrase: The reason phrase (e.g., "OK", "Not Found").
        description: A longer description of the status code.
    """

    _phrase: str
    _description: str

    def __new__(
        cls,
        value: int,
        phrase: str = "",
        description: str = "",
    ) -> HTTPStatus:
        obj = int.__new__(cls, value)
        obj._value_ = value
        obj._phrase = phrase
        obj._description = description
        return obj

    @property
    def phrase(self) -> str:
        """The reason phrase for this status code."""
        return self._phrase

    @property
    def description(self) -> str:
        """A longer description of this status code."""
        return self._description

    @property
    def is_informational(self) -> bool:
        """True if status code is 1xx (informational)."""
        return 100 <= int(self) < 200

    @property
    def is_success(self) -> bool:
        """True if status code is 2xx (success)."""
        return 200 <= int(self) < 300

    @property
    def is_redirect(self) -> bool:
        """True if status code is 3xx (redirection)."""
        return 300 <= int(self) < 400

    @property
    def is_client_error(self) -> bool:
        """True if status code is 4xx (client error)."""
        return 400 <= int(self) < 500

    @property
    def is_server_error(self) -> bool:
        """True if status code is 5xx (server error)."""
        return 500 <= int(self) < 600

    # 1xx Informational
    CONTINUE = (
        100,
        "Continue",
        "Request received, please continue.",
    )
    SWITCHING_PROTOCOLS = (
        101,
        "Switching Protocols",
        "Switching to new protocol; obey Upgrade header.",
    )
    PROCESSING = (
        102,
        "Processing",
        "Server has received and is processing the request.",
    )
    EARLY_HINTS = (
        103,
        "Early Hints",
        "Used to return some response headers before final response.",
    )

    # 2xx Success
    OK = (
        200,
        "OK",
        "Request fulfilled, document follows.",
    )
    CREATED = (
        201,
        "Created",
        "Document created, URL follows.",
    )
    ACCEPTED = (
        202,
        "Accepted",
        "Request accepted, processing continues off-line.",
    )
    NON_AUTHORITATIVE_INFORMATION = (
        203,
        "Non-Authoritative Information",
        "Request fulfilled from cache.",
    )
    NO_CONTENT = (
        204,
        "No Content",
        "Request fulfilled, nothing follows.",
    )
    RESET_CONTENT = (
        205,
        "Reset Content",
        "Clear input form for further input.",
    )
    PARTIAL_CONTENT = (
        206,
        "Partial Content",
        "Partial resource return due to request header.",
    )
    MULTI_STATUS = (
        207,
        "Multi-Status",
        "XML document containing multiple status codes.",
    )
    ALREADY_REPORTED = (
        208,
        "Already Reported",
        "Results previously returned.",
    )
    IM_USED = (
        226,
        "IM Used",
        "Request fulfilled, response is instance-manipulation.",
    )

    # 3xx Redirection
    MULTIPLE_CHOICES = (
        300,
        "Multiple Choices",
        "Multiple resources match the request.",
    )
    MOVED_PERMANENTLY = (
        301,
        "Moved Permanently",
        "Resource has permanently moved to a new URL.",
    )
    FOUND = (
        302,
        "Found",
        "Resource temporarily resides at a different URL.",
    )
    SEE_OTHER = (
        303,
        "See Other",
        "Response to request can be found at a different URL.",
    )
    NOT_MODIFIED = (
        304,
        "Not Modified",
        "Resource has not been modified since last request.",
    )
    USE_PROXY = (
        305,
        "Use Proxy",
        "Must use proxy to access resource.",
    )
    TEMPORARY_REDIRECT = (
        307,
        "Temporary Redirect",
        "Resource temporarily resides at a different URL.",
    )
    PERMANENT_REDIRECT = (
        308,
        "Permanent Redirect",
        "Resource has permanently moved to a new URL.",
    )

    # 4xx Client Error
    BAD_REQUEST = (
        400,
        "Bad Request",
        "Server cannot process request due to client error.",
    )
    UNAUTHORIZED = (
        401,
        "Unauthorized",
        "Authentication required and has failed or not been provided.",
    )
    PAYMENT_REQUIRED = (
        402,
        "Payment Required",
        "Reserved for future use.",
    )
    FORBIDDEN = (
        403,
        "Forbidden",
        "Server refuses to authorize the request.",
    )
    NOT_FOUND = (
        404,
        "Not Found",
        "Requested resource could not be found.",
    )
    METHOD_NOT_ALLOWED = (
        405,
        "Method Not Allowed",
        "Request method not allowed for the resource.",
    )
    NOT_ACCEPTABLE = (
        406,
        "Not Acceptable",
        "Resource not capable of generating acceptable content.",
    )
    PROXY_AUTHENTICATION_REQUIRED = (
        407,
        "Proxy Authentication Required",
        "Proxy authentication required.",
    )
    REQUEST_TIMEOUT = (
        408,
        "Request Timeout",
        "Server timed out waiting for the request.",
    )
    CONFLICT = (
        409,
        "Conflict",
        "Request conflicts with current state of the resource.",
    )
    GONE = (
        410,
        "Gone",
        "Resource is no longer available and has no forwarding address.",
    )
    LENGTH_REQUIRED = (
        411,
        "Length Required",
        "Content-Length header required.",
    )
    PRECONDITION_FAILED = (
        412,
        "Precondition Failed",
        "Precondition in request header evaluated to false.",
    )
    CONTENT_TOO_LARGE = (
        413,
        "Content Too Large",
        "Request entity is larger than server is willing to process.",
    )
    URI_TOO_LONG = (
        414,
        "URI Too Long",
        "Request URI is longer than server is willing to interpret.",
    )
    UNSUPPORTED_MEDIA_TYPE = (
        415,
        "Unsupported Media Type",
        "Request entity media type not supported.",
    )
    RANGE_NOT_SATISFIABLE = (
        416,
        "Range Not Satisfiable",
        "Requested range not satisfiable.",
    )
    EXPECTATION_FAILED = (
        417,
        "Expectation Failed",
        "Expect header requirement cannot be met.",
    )
    IM_A_TEAPOT = (
        418,
        "I'm a Teapot",
        "Server refuses to brew coffee because it is a teapot.",
    )
    MISDIRECTED_REQUEST = (
        421,
        "Misdirected Request",
        "Request directed at server unable to produce response.",
    )
    UNPROCESSABLE_ENTITY = (
        422,
        "Unprocessable Entity",
        "Request well-formed but contains semantic errors.",
    )
    LOCKED = (
        423,
        "Locked",
        "Resource is locked.",
    )
    FAILED_DEPENDENCY = (
        424,
        "Failed Dependency",
        "Request failed due to failure of a previous request.",
    )
    TOO_EARLY = (
        425,
        "Too Early",
        "Server unwilling to risk processing potentially replayed request.",
    )
    UPGRADE_REQUIRED = (
        426,
        "Upgrade Required",
        "Client should switch to a different protocol.",
    )
    PRECONDITION_REQUIRED = (
        428,
        "Precondition Required",
        "Origin server requires conditional request.",
    )
    TOO_MANY_REQUESTS = (
        429,
        "Too Many Requests",
        "User has sent too many requests in a given time.",
    )
    REQUEST_HEADER_FIELDS_TOO_LARGE = (
        431,
        "Request Header Fields Too Large",
        "Server unwilling to process due to large header fields.",
    )
    UNAVAILABLE_FOR_LEGAL_REASONS = (
        451,
        "Unavailable For Legal Reasons",
        "Resource unavailable due to legal demands.",
    )

    # 5xx Server Error
    INTERNAL_SERVER_ERROR = (
        500,
        "Internal Server Error",
        "Server encountered an unexpected condition.",
    )
    NOT_IMPLEMENTED = (
        501,
        "Not Implemented",
        "Server does not support the functionality required.",
    )
    BAD_GATEWAY = (
        502,
        "Bad Gateway",
        "Server received invalid response from upstream server.",
    )
    SERVICE_UNAVAILABLE = (
        503,
        "Service Unavailable",
        "Server currently unable to handle the request.",
    )
    GATEWAY_TIMEOUT = (
        504,
        "Gateway Timeout",
        "Server did not receive timely response from upstream.",
    )
    HTTP_VERSION_NOT_SUPPORTED = (
        505,
        "HTTP Version Not Supported",
        "Server does not support the HTTP version used.",
    )
    VARIANT_ALSO_NEGOTIATES = (
        506,
        "Variant Also Negotiates",
        "Content negotiation resulted in circular reference.",
    )
    INSUFFICIENT_STORAGE = (
        507,
        "Insufficient Storage",
        "Server unable to store the representation.",
    )
    LOOP_DETECTED = (
        508,
        "Loop Detected",
        "Server detected infinite loop while processing.",
    )
    NOT_EXTENDED = (
        510,
        "Not Extended",
        "Further extensions required for the request.",
    )
    NETWORK_AUTHENTICATION_REQUIRED = (
        511,
        "Network Authentication Required",
        "Client needs to authenticate to gain network access.",
    )
