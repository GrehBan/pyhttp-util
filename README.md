# pyhttp-util

**pyhttp-util** is a robust, strictly-typed Python library designed to simplify and standardize the manipulation of HTTP headers, authentication, and timeout configurations. It ensures compliance with RFC 7230 and provides a developer-friendly API for building and validating HTTP-related data structures.

## Features

*   **Strict Validation**: Enforces RFC 7230 rules for header names and values, preventing common HTTP vulnerabilities (like CRLF injection).
*   **Typed Data Structures**: Uses `dataclasses` and `enums` for predictable, type-safe code.
*   **Case-Insensitive Headers**: Built on top of `multidict`, allowing case-insensitive header lookups while preserving insertion order.
*   **Builders & Enums**: Includes a comprehensive `HTTPHeader` enum and a `HeaderBuilder` factory to avoid magic strings and typos.
*   **Basic Authentication**: Utilities for encoding and decoding HTTP Basic Auth credentials.
*   **Bearer Authentication**: Utilities for encoding and decoding Bearer tokens.
*   **Timeout Configuration**: a unified structure for managing connection and read timeouts.

## Installation

```bash
pip install pyhttp-util
```

## Usage

### 1. Working with Headers

The core of the library is the `Headers` collection and the `Header` item.

```python
from pyhttp_util.headers import Headers, Header, HeaderBuilder, HTTPHeader
from pyhttp_util.headers.validator import ValidationError

# --- Creating Headers ---

# Using the Builder (Recommended for standard headers)
h1 = HeaderBuilder.content_type("application/json")
h2 = HeaderBuilder.user_agent("MyClient/1.0")

# Manual creation
h3 = Header("X-Custom-Token", "123456")

# Using the Enum directly
h4 = Header(HTTPHeader.CACHE_CONTROL, "no-cache")

# --- Using the Collection ---

headers = Headers()
headers.add(h1)
headers.add(h2)
headers.add(h3)
headers.add(h4)

# Case-insensitive access
print(headers["content-type"])  # Output: application/json
print(headers.get("USER-AGENT")) # Output: MyClient/1.0

# Adding raw values
headers.add_raw("X-Debug", "True")

# Iterating
for h in headers:
    print(f"{h.name}: {h.value}")
```

### 2. Validation

The library validates headers upon creation to ensure safety.

```python
try:
    # This will raise a ValidationError because of the newline (CRLF injection protection)
    invalid_header = Header("X-Bad-Input", "value\r\nSet-Cookie: evil")
except ValidationError as e:
    print(f"Validation Error: {e}")

try:
    # Validating strictly against duplicates (if configured)
    strict_headers = Headers(allow_duplicates=False)
    strict_headers.add_raw("Content-Type", "application/json")
    strict_headers.add_raw("Content-Type", "text/plain") # Raises error
except ValidationError as e:
    print(f"Duplicate Error: {e}")
```

### 3. Authentication

Handle Basic and Bearer Auth easily and safely.

```python
from pyhttp_util.auth import BasicAuth, BearerAuth

# --- Basic Auth ---

# Encoding (Client side)
credentials = BasicAuth(login="user", password="password123")
auth_header_value = credentials.encode()
print(auth_header_value) 
# Output: Basic dXNlcjpwYXNzd29yZDEyMw==

# Decoding (Server side)
received_header = "Basic dXNlcjpwYXNzd29yZDEyMw=="
decoded = BasicAuth.decode(received_header)
print(f"User: {decoded.login}, Password: {decoded.password}")

# --- Bearer Auth ---

# Encoding
token_auth = BearerAuth(token="my-secret-token")
print(token_auth.encode())
# Output: Bearer my-secret-token

# Decoding
bearer_header = "Bearer my-secret-token"
decoded_token = BearerAuth.decode(bearer_header)
print(f"Token: {decoded_token.token}")
```

### 4. Timeouts

Configure timeouts for your HTTP clients.

```python
from pyhttp_util.timeout import Timeout

# Create a simple total timeout
t1 = Timeout.create(total=30.0)

# Granular configuration
t2 = Timeout(
    connect=5.0,
    sock_read=10.0,
    total=60.0
)
```

## Development

To run the project locally:

1.  **Clone the repository.**
2.  **Install dependencies:**
    ```bash
    uv sync
    ```
3.  **Run the demo:**
    ```bash
    uv run main.py
    ```

## License

MIT