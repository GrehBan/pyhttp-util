"HTTP Cookie management."

from collections.abc import Iterator
from dataclasses import dataclass
from datetime import datetime, timedelta, timezone
from enum import Enum

from pyhttp_util.headers.validator import RFC7230Validator, ValidationError

__all__ = ("SameSite", "Cookie", "CookieJar")


class SameSite(str, Enum):
    """Enumeration for SameSite cookie attribute."""

    LAX = "Lax"
    STRICT = "Strict"
    NONE = "None"


@dataclass
class Cookie:
    """Represents an HTTP Cookie.

    Attributes:
        name: The name of the cookie.
        value: The value of the cookie.
        domain: The domain the cookie applies to.
        path: The path the cookie applies to (default "/").
        expires: The expiration datetime.
        max_age: The max age in seconds.
        secure: Whether the cookie is secure-only.
        httponly: Whether the cookie is HTTP-only.
        samesite: The SameSite policy.
        partitioned: Whether the cookie is partitioned.
    """

    name: str
    value: str
    domain: str | None = None
    path: str = "/"
    expires: datetime | None = None
    max_age: int | None = None
    secure: bool = False
    httponly: bool = False
    samesite: SameSite | None = None
    partitioned: bool = False

    def __post_init__(self) -> None:
        """Validates the cookie attributes upon initialization."""
        RFC7230Validator.validate_field_name(self.name, raise_on_error=True)

        if not self._is_valid_cookie_value(self.value):
            raise ValidationError(f"Invalid cookie value: {self.value!r}")

    @staticmethod
    def _is_valid_cookie_value(value: str) -> bool:
        """Validates cookie value according to RFC 6265.

        cookie-value      = *cookie-octet / ( DQUOTE *cookie-octet DQUOTE )
        cookie-octet      = %x21 / %x23-2B / %x2D-3A / %x3C-5B / %x5D-7E

        Args:
            value: The cookie value to validate.

        Returns:
            True if valid, False otherwise.
        """
        if not value:
            return True

        if len(value) >= 2 and value.startswith('"') and value.endswith('"'):
            value = value[1:-1]

        forbidden = {",", ";", "\\", '"'}
        for char in value:
            code = ord(char)
            if code <= 0x20 or code >= 0x7F or char in forbidden:
                return False
        return True

    def __str__(self) -> str:
        """Returns the Set-Cookie header value string.

        Returns:
            The formatted Set-Cookie header value.
        """
        parts = [f"{self.name}={self.value}"]

        if self.domain:
            parts.append(f"Domain={self.domain}")

        if self.path:
            parts.append(f"Path={self.path}")

        if self.expires:
            dt = self.expires
            if dt.tzinfo is None:
                dt = dt.replace(tzinfo=timezone.utc)
            else:
                dt = dt.astimezone(timezone.utc)
            parts.append(f"Expires={dt.strftime('%a, %d %b %Y %H:%M:%S GMT')}")

        if self.max_age is not None:
            parts.append(f"Max-Age={self.max_age}")

        if self.secure:
            parts.append("Secure")

        if self.httponly:
            parts.append("HttpOnly")

        if self.samesite:
            parts.append(f"SameSite={self.samesite}")

        if self.partitioned:
            parts.append("Partitioned")

        return "; ".join(parts)


class CookieJar:
    """A container for managing and filtering cookies."""

    def __init__(self) -> None:
        """Initializes an empty CookieJar."""
        self._cookies: list[Cookie] = []

    def add(self, cookie: Cookie) -> None:
        """Adds a cookie to the jar.

        Replaces existing cookies with the same name, domain, and path.
        Calculates 'expires' from 'max_age' if needed.

        Args:
            cookie: The Cookie object to add.
        """
        if cookie.max_age is not None and cookie.expires is None:
            now = datetime.now(timezone.utc)
            cookie.expires = now + timedelta(seconds=cookie.max_age)

        self.discard(cookie.name, cookie.domain, cookie.path)
        self._cookies.append(cookie)

    def discard(
        self, name: str, domain: str | None = None, path: str = "/"
    ) -> None:
        """Removes a cookie from the jar.

        Args:
            name: The cookie name.
            domain: The cookie domain (optional).
            path: The cookie path (default "/").
        """
        self._cookies = [
            c
            for c in self._cookies
            if not (c.name == name and c.domain == domain and c.path == path)
        ]

    def clear(self) -> None:
        """Clears all cookies from the jar."""
        self._cookies.clear()

    def filter(
        self, domain: str, path: str = "/", secure: bool = False
    ) -> list[Cookie]:
        """Returns a list of cookies that match the given request context.

        Also removes expired cookies from the jar.

        Args:
            domain: The request domain.
            path: The request path.
            secure: Whether the request is secure (HTTPS).

        Returns:
            A list of matching Cookie objects, sorted by path length.
        """
        matches = []
        now = datetime.now(timezone.utc)
        to_remove = []

        for cookie in self._cookies:
            if cookie.expires:
                dt = cookie.expires
                if dt.tzinfo is None:
                    dt = dt.replace(tzinfo=timezone.utc)
                if dt < now:
                    to_remove.append(cookie)
                    continue

            if cookie.domain:
                if not self._domain_match(domain, cookie.domain):
                    continue

            if not self._path_match(path, cookie.path):
                continue

            if cookie.secure and not secure:
                continue

            matches.append(cookie)

        for c in to_remove:
            if c in self._cookies:
                self._cookies.remove(c)

        matches.sort(key=lambda c: len(c.path), reverse=True)
        return matches

    def output(
        self, domain: str, path: str = "/", secure: bool = False
    ) -> str:
        """Returns the Cookie header value for the given request context.

        Args:
            domain: The request domain.
            path: The request path.
            secure: Whether the request is secure.

        Returns:
            The formatted Cookie header string.
        """
        cookies = self.filter(domain, path, secure)
        return "; ".join(f"{c.name}={c.value}" for c in cookies)

    @staticmethod
    def _domain_match(request_domain: str, cookie_domain: str) -> bool:
        """Performs RFC 6265 5.1.3 Domain Matching.

        Args:
            request_domain: The domain of the request.
            cookie_domain: The domain attribute of the cookie.

        Returns:
            True if matching, False otherwise.
        """
        request_domain = request_domain.lower()
        cookie_domain = cookie_domain.lower()

        if cookie_domain.startswith("."):
            cookie_domain = cookie_domain[1:]

        if request_domain == cookie_domain:
            return True

        if request_domain.endswith("." + cookie_domain):
            return True

        return False

    @staticmethod
    def _path_match(request_path: str, cookie_path: str) -> bool:
        """Performs RFC 6265 5.1.4 Path Matching.

        Args:
            request_path: The path of the request.
            cookie_path: The path attribute of the cookie.

        Returns:
            True if matching, False otherwise.
        """
        if request_path == cookie_path:
            return True

        if request_path.startswith(cookie_path):
            if cookie_path.endswith("/"):
                return True
            if request_path[len(cookie_path)] == "/":
                return True

        return False

    def __iter__(self) -> Iterator[Cookie]:
        """Returns an iterator over all cookies in the jar.

        Returns:
            An iterator of Cookie objects.
        """
        return iter(self._cookies)

    def __len__(self) -> int:
        """Returns the number of cookies in the jar.

        Returns:
            The count of cookies.
        """
        return len(self._cookies)
