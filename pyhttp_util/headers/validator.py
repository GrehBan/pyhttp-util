"RFC 7230 and related standards validator for HTTP headers."

from __future__ import annotations

import re
from collections.abc import Sequence
from dataclasses import dataclass
from typing import Any

__all__ = ("RFC7230Validator", "ValidationError", "ValidationResult")


class ValidationError(Exception):
    """Exception raised for validation errors."""

    pass


@dataclass(frozen=True, slots=True)
class ValidationResult:
    """Result of a validation operation.

    Attributes:
        valid: Whether the validation was successful.
        error: The error message if validation failed.
    """

    valid: bool
    error: str | None = None

    def __bool__(self) -> bool:
        """Returns True if valid, False otherwise."""
        return self.valid


class RFC7230Validator:
    """Validator for HTTP headers
    according to RFC 7230 and related standards."""

    TCHAR_PATTERN = re.compile(r'^[!#$%&\'"*+\-.0-9A-Z^_`a-z|~]+\Z')

    VCHAR_MIN = 0x21
    VCHAR_MAX = 0x7E
    OBS_TEXT_MIN = 0x80
    OBS_TEXT_MAX = 0xFF

    SP = 0x20
    HTAB = 0x09

    ALLOWED_DUPLICATES = {"set-cookie"}

    COMMA_SEPARATED_HEADERS = {
        "accept",
        "accept-charset",
        "accept-encoding",
        "accept-language",
        "allow",
        "cache-control",
        "connection",
        "content-encoding",
        "content-language",
        "expect",
        "if-match",
        "if-none-match",
        "pragma",
        "proxy-authenticate",
        "te",
        "trailer",
        "transfer-encoding",
        "upgrade",
        "vary",
        "via",
        "warning",
        "www-authenticate",
        "access-control-allow-headers",
        "access-control-allow-methods",
        "access-control-expose-headers",
        "access-control-request-headers",
    }

    @classmethod
    def validate_field_name(
        cls, name: str, raise_on_error: bool = False
    ) -> ValidationResult:
        """Validates a header field name.

        Args:
            name: The header name to validate.
            raise_on_error: Whether to raise ValidationError on failure.

        Returns:
            ValidationResult: The result of validation.

        Raises:
            ValidationError: If invalid and raise_on_error is True.
        """
        if not name:
            error = "Header name cannot be empty"
            if raise_on_error:
                raise ValidationError(error)
            return ValidationResult(False, error)

        if name[0] in (" ", "\t"):
            error = f"Header name cannot start with whitespace: {name!r}"
            if raise_on_error:
                raise ValidationError(error)
            return ValidationResult(False, error)

        if name[-1] in (" ", "\t"):
            error = f"Header name cannot end with whitespace: {name!r}"
            if raise_on_error:
                raise ValidationError(error)
            return ValidationResult(False, error)

        if not cls.TCHAR_PATTERN.match(name):
            error = f"Header name contains invalid characters: {name!r}."
            if raise_on_error:
                raise ValidationError(error)
            return ValidationResult(False, error)

        return ValidationResult(True)

    @classmethod
    def validate_field_value(
        cls,
        value: str,
        raise_on_error: bool = False,
        allow_obs_fold: bool = False,
    ) -> ValidationResult:
        """Validates a header field value.

        Args:
            value: The header value to validate.
            raise_on_error: Whether to raise ValidationError on failure.
            allow_obs_fold: Whether to allow obsolete line folding.

        Returns:
            ValidationResult: The result of validation.

        Raises:
            ValidationError: If invalid and raise_on_error is True.
        """
        if not value:
            return ValidationResult(True)

        if not allow_obs_fold and "\r\n" in value:
            error = (
                f"Header value contains deprecated "
                f"line folding (obs-fold): {value!r}"
            )
            if raise_on_error:
                raise ValidationError(error)
            return ValidationResult(False, error)

        for i, char in enumerate(value):
            char_code = ord(char)

            is_valid = (
                (cls.VCHAR_MIN <= char_code <= cls.VCHAR_MAX)
                or (cls.OBS_TEXT_MIN <= char_code <= cls.OBS_TEXT_MAX)
                or (char_code == cls.SP)
                or (char_code == cls.HTAB)
            )

            if not is_valid:
                if allow_obs_fold and char in ("\r", "\n"):
                    continue

                error = (
                    f"Header value contains invalid "
                    f"character at position {i}: {char!r} (0x{char_code:02X})"
                )
                if raise_on_error:
                    raise ValidationError(error)
                return ValidationResult(False, error)

        return ValidationResult(True)

    @classmethod
    def validate_header_field(
        cls, name: str, value: str, raise_on_error: bool = False
    ) -> ValidationResult:
        """Validates both header name and value.

        Args:
            name: The header name.
            value: The header value.
            raise_on_error: Whether to raise ValidationError on failure.

        Returns:
            ValidationResult: The result of validation.

        Raises:
            ValidationError: If invalid and raise_on_error is True.
        """
        name_result = cls.validate_field_name(name, raise_on_error=False)
        if not name_result:
            if raise_on_error:
                raise ValidationError(name_result.error)
            return name_result

        stripped_value = value.strip(" \t")
        value_result = cls.validate_field_value(
            stripped_value, raise_on_error=False
        )
        if not value_result:
            if raise_on_error:
                raise ValidationError(value_result.error)
            return value_result

        return ValidationResult(True)

    @classmethod
    def normalize_field_value(cls, value: str) -> str:
        """Normalizes a header field value by stripping whitespace.

        Args:
            value: The value to normalize.

        Returns:
            str: The normalized value.
        """
        return value.strip(" \t")

    @classmethod
    def validate_no_duplicate_headers(
        cls,
        headers: Sequence[tuple[Any, str]],
        raise_on_error: bool = False,
    ) -> ValidationResult:
        """Validates that there are no disallowed duplicate headers.

        Args:
            headers: Sequence of (name, value) tuples. Names can be str or
                any type with a lower() method (e.g., HTTPHeader, istr).
            raise_on_error: Whether to raise ValidationError on failure.

        Returns:
            ValidationResult: The result of validation.

        Raises:
            ValidationError: If invalid and raise_on_error is True.
        """
        seen = {}
        for name, value in headers:
            name_lower = name.lower()

            if name_lower in seen:
                if name_lower in cls.ALLOWED_DUPLICATES:
                    continue

                if name_lower in cls.COMMA_SEPARATED_HEADERS:
                    error = (
                        f"Duplicate header '{name}' should be combined with "
                        f"comma separation instead of multiple header fields"
                    )
                    if raise_on_error:
                        raise ValidationError(error)
                    return ValidationResult(False, error)

                error = f"Duplicate header field not allowed: '{name}'"
                if raise_on_error:
                    raise ValidationError(error)
                return ValidationResult(False, error)

            seen[name_lower] = value

        return ValidationResult(True)

    @classmethod
    def validate_header_size(
        cls,
        name: str,
        value: str,
        max_size: int = 8192,
        raise_on_error: bool = False,
    ) -> ValidationResult:
        """Validates that the header size is within limits.

        Args:
            name: The header name.
            value: The header value.
            max_size: Maximum size in bytes.
            raise_on_error: Whether to raise ValidationError on failure.

        Returns:
            ValidationResult: The result of validation.

        Raises:
            ValidationError: If invalid and raise_on_error is True.
        """
        header_size = (
            len(name.encode("utf-8")) + 2 + len(value.encode("utf-8")) + 2
        )

        if header_size > max_size:
            error = (
                f"Header size {header_size} bytes "
                f"exceeds maximum {max_size} bytes"
            )
            if raise_on_error:
                raise ValidationError(error)
            return ValidationResult(False, error)

        return ValidationResult(True)
