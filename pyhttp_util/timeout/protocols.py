"""Protocol definitions for timeout module.

No specific RFC - timeouts are implementation-defined.
"""

from typing import Protocol, TypeAlias, runtime_checkable

__all__ = ("RawTimeoutType", "TimeoutType", "TimeoutProtocol")

RawTimeoutType: TypeAlias = int | float
TimeoutType: TypeAlias = RawTimeoutType | "TimeoutProtocol"


@runtime_checkable
class TimeoutProtocol(Protocol):
    """Protocol for timeout configuration."""

    total: RawTimeoutType | None
    connect: RawTimeoutType | None
    sock_connect: RawTimeoutType | None
    sock_read: RawTimeoutType | None