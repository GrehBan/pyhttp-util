"""HTTP methods and descriptions.

RFC 9110: HTTP Semantics
https://datatracker.ietf.org/doc/html/rfc9110

RFC 5789: PATCH Method for HTTP
https://datatracker.ietf.org/doc/html/rfc5789
"""

from __future__ import annotations

from enum import Enum

__all__ = ("HTTPMethod",)


class HTTPMethod(str, Enum):
    """HTTP methods and descriptions.

    RFC 9110: GET, HEAD, POST, PUT, DELETE, CONNECT, OPTIONS, TRACE
    RFC 5789: PATCH
    """

    _description: str

    def __new__(cls, value: str, description: str) -> HTTPMethod:
        obj = str.__new__(cls, value)
        obj._value_ = value
        obj._description = description
        return obj

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__}.{self._name_}>"

    CONNECT = ("CONNECT", "Establish a connection to the server.")
    DELETE = ("DELETE", "Remove the target.")
    GET = ("GET", "Retrieve the target.")
    HEAD = (
        "HEAD",
        "Same as GET, but only retrieve the status line and header section.",
    )
    OPTIONS = ("OPTIONS", "Describe the communication options for the target.")
    PATCH = ("PATCH", "Apply partial modifications to a target.")
    POST = (
        "POST",
        "Perform target-specific processing with the request payload.",
    )
    PUT = ("PUT", "Replace the target with the request payload.")
    TRACE = (
        "TRACE",
        "Perform a message loop-back test along the path to the target.",
    )

    @property
    def description(self) -> str:
        """Return the description of the method."""
        return self._description
