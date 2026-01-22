"HTTP Basic Authentication utilities."

from __future__ import annotations

import base64
import binascii
from dataclasses import dataclass

from pyhttp_util.headers.headers import Header, HeaderType

__all__ = ("BasicAuth",)

DEFAULT_ENCODING = "latin1"


@dataclass(frozen=True, slots=True)
class BasicAuth:
    """HTTP Basic Authentication credentials."""

    login: str
    password: str
    encoding: str = DEFAULT_ENCODING

    def __post_init__(self) -> None:
        """Validates that login does not contain a colon."""
        if ":" in self.login:
            raise ValueError("User ID cannot contain a colon")

    @classmethod
    def decode(
        cls, header: HeaderType, encoding: str = DEFAULT_ENCODING
    ) -> BasicAuth:
        """Create a BasicAuth object from an Authorization HTTP header.

        Args:
            header: The Authorization header (string or Header object).
            encoding: The encoding to use for decoding credentials.

        Returns:
            A BasicAuth instance.

        Raises:
            ValueError: If the header is invalid (not Basic auth, malformed).
        """
        if isinstance(header, Header):
            auth_str = header.value
        else:
            auth_str = header

        if not auth_str:
            raise ValueError("Empty authorization header")

        try:
            auth_type, credentials = auth_str.split(" ", 1)
        except ValueError:
            raise ValueError(
                f"Invalid authorization header format: '{auth_str}'"
            ) from None

        if auth_type.lower() != "basic":
            raise ValueError(
                f"Authentication type must be Basic, got: '{auth_type}'"
            )

        try:
            decoded_bytes = base64.b64decode(credentials.strip())
            decoded_str = decoded_bytes.decode(encoding)
        except (binascii.Error, UnicodeDecodeError) as e:
            raise ValueError(f"Invalid credentials encoding: {e}") from e

        if ":" not in decoded_str:
            raise ValueError(
                "Invalid credentials format: missing colon separator"
            )

        login, password = decoded_str.split(":", 1)
        return cls(login=login, password=password, encoding=encoding)

    def encode(self) -> str:
        """Encode credentials into the Authorization header value.

        Returns:
            The string "Basic <base64-encoded-credentials>".
        """
        credentials = f"{self.login}:{self.password}"
        encoded_bytes = base64.b64encode(credentials.encode(self.encoding))
        return f"Basic {encoded_bytes.decode(self.encoding)}"

    def __str__(self) -> str:
        """Returns the encoded Authorization header value."""
        return self.encode()
