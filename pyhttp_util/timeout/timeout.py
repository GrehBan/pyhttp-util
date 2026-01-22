from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class Timeout:
    """
    Timeout configuration.

    Attributes:
        total: Total timeout for the entire operation.
        connect: Timeout for establishing a connection
        sock_connect: Timeout for the socket connection phase specifically.
        sock_read: Timeout for reading data from the socket.
    """

    total: float | None = None
    connect: float | None = None
    sock_connect: float | None = None
    sock_read: float | None = None

    def __post_init__(self) -> None:
        """Validates that all timeout values are non-negative."""
        for field_name in ("total", "connect", "sock_connect", "sock_read"):
            val = getattr(self, field_name)
            if val is not None and val < 0:
                raise ValueError(
                    f"'{field_name}' must be non-negative, got {val}"
                )

    @classmethod
    def create(cls, total: float | None) -> "Timeout":
        """
        Create a Timeout instance with a total timeout.

        Args:
            total: The total timeout value.

        Returns:
            A new Timeout instance.
        """
        return cls(total=total)
