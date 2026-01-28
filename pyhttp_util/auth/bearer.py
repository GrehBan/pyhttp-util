"""HTTP Bearer Token Authentication utilities.

RFC 6750: The OAuth 2.0 Authorization Framework: Bearer Token Usage
https://datatracker.ietf.org/doc/html/rfc6750
"""

from __future__ import annotations

from dataclasses import dataclass

from pyhttp_util.headers.headers import Header, HeaderType

__all__ = ("BearerAuth",)


@dataclass(frozen=True, slots=True)
class BearerAuth:
    """HTTP Bearer Authentication token (RFC 6750)."""

    token: str

    def __post_init__(self) -> None:
        """Validates that token is not empty and has no whitespace."""
        if not self.token:
            raise ValueError("Token cannot be empty")
        if any(char.isspace() for char in self.token):
            raise ValueError("Token cannot contain whitespace")

    @classmethod
    def decode(cls, header: HeaderType) -> BearerAuth:
        """Create a BearerAuth object from an Authorization HTTP header.

        Args:
            header: The Authorization header (string or Header object).

        Returns:
            A BearerAuth instance.

        Raises:
            ValueError: If the header is invalid (not Bearer auth, malformed).
        """
        if isinstance(header, Header):
            auth_str = header.value
        else:
            auth_str = header

        if not auth_str:
            raise ValueError("Empty authorization header")

        try:
            auth_type, token = auth_str.split(" ", 1)
        except ValueError:
            raise ValueError(
                f"Invalid authorization header format: '{auth_str}'"
            ) from None

        if auth_type.lower() != "bearer":
            raise ValueError(
                f"Authentication type must be Bearer, got: '{auth_type}'"
            )

        token = token.strip()
        if not token:
            raise ValueError("Empty token in authorization header")

        return cls(token=token)

    def encode(self) -> str:
        """Encode credentials into the Authorization header value.

        Returns:
            The string "Bearer <token>".
        """
        return f"Bearer {self.token}"

    def __str__(self) -> str:
        """Returns the encoded Authorization header value."""
        return self.encode()
