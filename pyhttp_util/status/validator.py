"""HTTP status code validation utilities.

RFC 9110: HTTP Semantics
https://datatracker.ietf.org/doc/html/rfc9110
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from pyhttp_util.status.exceptions import get_exception_for_status
from pyhttp_util.status.status_enum import HTTPStatus

__all__ = (
    "StatusCodeValidator",
    "StatusValidationError",
    "StatusValidationResult",
)


class StatusValidationError(Exception):
    """Exception raised for status code validation errors."""

    pass


@dataclass(frozen=True, slots=True)
class StatusValidationResult:
    """Result of a status code validation.

    Attributes:
        valid: Whether the status code is valid.
        error: Error message if validation failed, None otherwise.
    """

    valid: bool
    error: str | None = None

    def __bool__(self) -> bool:
        return self.valid


StatusCategory = Literal[
    "informational",
    "success",
    "redirect",
    "client_error",
    "server_error",
    "unknown",
]


class StatusCodeValidator:
    """Validator for HTTP status codes (RFC 9110 Section 15).

    Provides methods to validate status codes, check their categories,
    and raise appropriate exceptions for error status codes.
    """

    MIN_STATUS_CODE = 100
    MAX_STATUS_CODE = 599

    # Set of all valid status codes from the enum
    _VALID_CODES: frozenset[int] = frozenset(
        member.value for member in HTTPStatus
    )

    @classmethod
    def validate(
        cls,
        code: int,
        raise_on_error: bool = False,
    ) -> StatusValidationResult:
        """Validate that a status code is within the valid range.

        Args:
            code: The HTTP status code to validate.
            raise_on_error: If True, raise StatusValidationError on failure.

        Returns:
            StatusValidationResult indicating validity.

        Raises:
            StatusValidationError: If raise_on_error is True and validation
                fails.
        """
        if not isinstance(code, int):
            error = (
                f"Status code must be an integer, got {type(code).__name__}"
            )
            if raise_on_error:
                raise StatusValidationError(error)
            return StatusValidationResult(False, error)

        if not cls.MIN_STATUS_CODE <= code <= cls.MAX_STATUS_CODE:
            error = (
                f"Status code {code} is outside valid range "
                f"({cls.MIN_STATUS_CODE}-{cls.MAX_STATUS_CODE})"
            )
            if raise_on_error:
                raise StatusValidationError(error)
            return StatusValidationResult(False, error)

        return StatusValidationResult(True)

    @classmethod
    def validate_standard(
        cls,
        code: int,
        raise_on_error: bool = False,
    ) -> StatusValidationResult:
        """Validate that a status code is a standard HTTP status code.

        This is stricter than validate() - it only accepts codes
        defined in the HTTPStatus enum.

        Args:
            code: The HTTP status code to validate.
            raise_on_error: If True, raise StatusValidationError on failure.

        Returns:
            StatusValidationResult indicating validity.

        Raises:
            StatusValidationError: If raise_on_error is True and validation
                fails.
        """
        result = cls.validate(code, raise_on_error)
        if not result:
            return result

        if code not in cls._VALID_CODES:
            error = f"Status code {code} is not a standard HTTP status code"
            if raise_on_error:
                raise StatusValidationError(error)
            return StatusValidationResult(False, error)

        return StatusValidationResult(True)

    @classmethod
    def validate_range(
        cls,
        code: int,
        min_code: int,
        max_code: int,
        raise_on_error: bool = False,
    ) -> StatusValidationResult:
        """Validate that a status code is within a specific range.

        Args:
            code: The HTTP status code to validate.
            min_code: Minimum allowed status code (inclusive).
            max_code: Maximum allowed status code (inclusive).
            raise_on_error: If True, raise StatusValidationError on failure.

        Returns:
            StatusValidationResult indicating validity.

        Raises:
            StatusValidationError: If raise_on_error is True and validation
                fails.
        """
        result = cls.validate(code, raise_on_error)
        if not result:
            return result

        if not min_code <= code <= max_code:
            error = (
                f"Status code {code} is outside range {min_code}-{max_code}"
            )
            if raise_on_error:
                raise StatusValidationError(error)
            return StatusValidationResult(False, error)

        return StatusValidationResult(True)

    @classmethod
    def is_valid(cls, code: int) -> bool:
        """Check if a status code is within the valid range.

        Args:
            code: The HTTP status code to check.

        Returns:
            True if the status code is valid, False otherwise.
        """
        return bool(cls.validate(code))

    @classmethod
    def is_standard(cls, code: int) -> bool:
        """Check if a status code is a standard HTTP status code.

        Args:
            code: The HTTP status code to check.

        Returns:
            True if the status code is standard, False otherwise.
        """
        return bool(cls.validate_standard(code))

    @classmethod
    def get_category(cls, code: int) -> StatusCategory:
        """Get the category of a status code.

        Args:
            code: The HTTP status code.

        Returns:
            The category name: "informational", "success", "redirect",
            "client_error", "server_error", or "unknown".
        """
        if 100 <= code < 200:
            return "informational"
        if 200 <= code < 300:
            return "success"
        if 300 <= code < 400:
            return "redirect"
        if 400 <= code < 500:
            return "client_error"
        if 500 <= code < 600:
            return "server_error"
        return "unknown"

    @classmethod
    def is_informational(cls, code: int) -> bool:
        """Check if status code is 1xx (informational)."""
        return 100 <= code < 200

    @classmethod
    def is_success(cls, code: int) -> bool:
        """Check if status code is 2xx (success)."""
        return 200 <= code < 300

    @classmethod
    def is_redirect(cls, code: int) -> bool:
        """Check if status code is 3xx (redirect)."""
        return 300 <= code < 400

    @classmethod
    def is_client_error(cls, code: int) -> bool:
        """Check if status code is 4xx (client error)."""
        return 400 <= code < 500

    @classmethod
    def is_server_error(cls, code: int) -> bool:
        """Check if status code is 5xx (server error)."""
        return 500 <= code < 600

    @classmethod
    def is_error(cls, code: int) -> bool:
        """Check if status code is an error (4xx or 5xx)."""
        return code >= 400

    @classmethod
    def raise_for_status(
        cls,
        code: int,
        message: str | None = None,
        full_range: bool = False,
    ) -> None:
        """Raise an appropriate exception for error status codes.

        raises the appropriate exception from the exception
        hierarchy.

        Args:
            code: The HTTP status code.
            message: Optional custom error message.
            full_range: flag for raise exception for full status code range

        Raises:
            HTTPStatusError instance based on the status code.
        """
        if code < 400 and full_range is False:
            return

        exc_class = get_exception_for_status(code)
        raise exc_class(message=message, status_code=code)

    @classmethod
    def get_status(cls, code: int) -> HTTPStatus | None:
        """Get the HTTPStatus enum member for a status code.

        Args:
            code: The HTTP status code.

        Returns:
            The HTTPStatus enum member, or None if not a standard code.
        """
        try:
            return HTTPStatus(code)
        except ValueError:
            return None

    @classmethod
    def get_phrase(cls, code: int) -> str | None:
        """Get the reason phrase for a status code.

        Args:
            code: The HTTP status code.

        Returns:
            The reason phrase, or None if not a standard code.
        """
        status = cls.get_status(code)
        return status.phrase if status else None

    @classmethod
    def get_description(cls, code: int) -> str | None:
        """Get the description for a status code.

        Args:
            code: The HTTP status code.

        Returns:
            The description, or None if not a standard code.
        """
        status = cls.get_status(code)
        return status.description if status else None
