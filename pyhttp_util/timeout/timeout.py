"""Timeout configuration for HTTP operations.

No specific RFC - timeouts are implementation-defined.
"""

from __future__ import annotations

from dataclasses import dataclass

from pyhttp_util.timeout.protocols import (
    RawTimeoutType,
    TimeoutProtocol,
    TimeoutType,
)

__all__ = ("Timeout",)


@dataclass(frozen=True, slots=True)
class Timeout:
    """Timeout configuration.

    Attributes:
        total: Total timeout for the entire operation.
        connect: Timeout for establishing a connection.
        sock_connect: Timeout for the socket connection phase specifically.
        sock_read: Timeout for reading data from the socket.
    """

    total: RawTimeoutType | None = None
    connect: RawTimeoutType | None = None
    sock_connect: RawTimeoutType | None = None
    sock_read: RawTimeoutType | None = None

    def __post_init__(self) -> None:
        """Validates that all timeout values are non-negative."""
        for field_name in ("total", "connect", "sock_connect", "sock_read"):
            val = getattr(self, field_name)
            if val is not None and val < 0:
                raise ValueError(
                    f"'{field_name}' must be non-negative, got {val}"
                )

    @classmethod
    def create(cls, total: float | None) -> Timeout:
        """Create a Timeout instance with a total timeout.

        Args:
            total: The total timeout value.

        Returns:
            A new Timeout instance.
        """
        return cls(total=total)

    @classmethod
    def normalize(cls, timeout: TimeoutType) -> Timeout:
        """Normalize a timeout to Timeout instance.

        Args:
            timeout: The raw timeout value or Timeout instance to normalize.

        Returns:
            A new Timeout instance with normalized values.

        Raises:
            TypeError: When timeout type is unsupported.
        """
        if isinstance(timeout, Timeout):
            return timeout

        if isinstance(timeout, (int, float)):
            return cls.create(timeout)
        if isinstance(timeout, TimeoutProtocol):
            return cls(
                total=timeout.total,
                connect=timeout.connect,
                sock_connect=timeout.sock_connect,
                sock_read=timeout.sock_read,
            )
        # Unreachable if TimeoutType is correct (defensive code)
        msg = f"Unsupported timeout type: {type(timeout)}"
        raise TypeError(msg)  # pragma: no cover