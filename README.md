# pyhttp-util

[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Typed](https://img.shields.io/badge/typed-mypy-blue.svg)](https://mypy-lang.org/)
[![Code style: ruff](https://img.shields.io/badge/code%20style-ruff-000000.svg)](https://github.com/astral-sh/ruff)

**pyhttp-util** is a robust, strictly-typed Python library designed to simplify and standardize the manipulation of HTTP headers, authentication, cookies, and timeout configurations. It ensures compliance with RFC 7230 and RFC 6265, and provides a developer-friendly API for building and validating HTTP-related data structures.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Quick Start](#quick-start)
- [Usage](#usage)
  - [Headers](#1-working-with-headers)
  - [Validation](#2-validation)
  - [Authentication](#3-authentication)
  - [Cookies](#4-cookies)
  - [Timeouts](#5-timeouts)
- [API Reference](#api-reference)
- [Development](#development)
- [License](#license)

## Features

- **Strict Validation**: Enforces RFC 7230 rules for header names and values, preventing common HTTP vulnerabilities (like CRLF injection)
- **Cookie Support**: Full RFC 6265 compliant cookie handling with `SameSite`, `Secure`, `HttpOnly`, and `Partitioned` attributes
- **Typed Data Structures**: Uses `dataclasses` and `enums` for predictable, type-safe code with full `mypy` strict mode support
- **Case-Insensitive Headers**: Built on top of `multidict`, allowing case-insensitive header lookups while preserving insertion order
- **Builders & Enums**: Includes a comprehensive `HTTPHeader` enum (100+ standard headers) and a `HeaderBuilder` factory to avoid magic strings and typos
- **Authentication**: Utilities for encoding and decoding HTTP Basic Auth and Bearer token credentials
- **Timeout Configuration**: A unified, immutable structure for managing connection, socket, and total timeouts
- **Zero Runtime Dependencies**: Only depends on `multidict` for case-insensitive dictionary support

## Installation

```bash
pip install pyhttp-util
```

Or with [uv](https://github.com/astral-sh/uv):

```bash
uv add pyhttp-util
```

## Quick Start

```python
from pyhttp_util import (
    Headers,
    Header,
    HeaderBuilder,
    HTTPHeader,
    BasicAuth,
    BearerAuth,
    Cookie,
    CookieJar,
    SameSite,
    Timeout,
)

# Create headers
headers = Headers()
headers.add(HeaderBuilder.content_type("application/json"))
headers.add(HeaderBuilder.authorization(BasicAuth("user", "pass").encode()))
headers.add_raw("X-Custom-Header", "custom-value")

# Case-insensitive access
print(headers["content-type"])  # application/json

# Create cookies
cookie = Cookie(
    name="session",
    value="abc123",
    secure=True,
    httponly=True,
    samesite=SameSite.STRICT,
)

# Configure timeouts
timeout = Timeout(total=30.0, connect=5.0, sock_read=10.0)
```

## Usage

### 1. Working with Headers

The core of the library is the `Headers` collection and the `Header` dataclass.

```python
from pyhttp_util.headers import Headers, Header, HeaderBuilder, HTTPHeader

# --- Creating Headers ---

# Using the Builder (Recommended for standard headers)
h1 = HeaderBuilder.content_type("application/json")
h2 = HeaderBuilder.user_agent("MyClient/1.0")
h3 = HeaderBuilder.accept("text/html, application/json")

# Manual creation with string name
h4 = Header("X-Custom-Token", "123456")

# Using the HTTPHeader enum directly
h5 = Header(HTTPHeader.CACHE_CONTROL, "no-cache, no-store")

# --- Using the Headers Collection ---

headers = Headers()
headers.add(h1)
headers.add(h2)
headers.add_raw("X-Request-ID", "req-12345")

# Case-insensitive access
print(headers["content-type"])      # application/json
print(headers.get("USER-AGENT"))    # MyClient/1.0
print(headers.get("missing"))       # None

# Check existence
if "content-type" in headers:
    print("Content-Type is set")

# Get all values for a header (useful for Set-Cookie, etc.)
all_values = headers.get_all("Set-Cookie")

# Iterate over headers
for header in headers:
    print(f"{header.name}: {header.value}")

# Dictionary-like operations
headers["X-New-Header"] = "new-value"  # Add or replace
del headers["X-Request-ID"]            # Remove

# Convert to different formats
as_dict = headers.to_dict()      # CIMultiDict
as_list = headers.to_list()      # list[Header]
as_tuples = headers.to_tuples()  # list[tuple[name, value]]

# Copy headers
headers_copy = headers.copy()

# Merge headers (keeps existing, adds missing)
other_headers = Headers()
other_headers.add_raw("Accept-Language", "en-US")
headers.merge(other_headers)
```

#### Building Headers from Different Sources

```python
# From a dictionary
headers = Headers.build_from_dict({
    "Content-Type": "application/json",
    "Accept": "application/json",
})

# From a list of tuples
headers = Headers.build_from_tuples([
    ("Content-Type", "application/json"),
    ("Accept", "application/json"),
])

# From a list of Header objects
headers = Headers.build_from_list([
    Header(HTTPHeader.CONTENT_TYPE, "application/json"),
    Header(HTTPHeader.ACCEPT, "application/json"),
])

# All build methods support allow_duplicates parameter
headers = Headers.build_from_dict(
    {"Content-Type": "application/json"},
    allow_duplicates=True
)
```

### 2. Validation

The library validates headers upon creation to ensure RFC 7230 compliance and security.

```python
from pyhttp_util.headers import Header, Headers
from pyhttp_util.headers.validator import (
    RFC7230Validator,
    ValidationError,
    ValidationResult,
)

# --- Automatic Validation on Creation ---

try:
    # CRLF injection protection - raises ValidationError
    invalid = Header("X-Bad", "value\r\nSet-Cookie: evil")
except ValidationError as e:
    print(f"Blocked: {e}")

try:
    # Invalid header name characters - raises ValidationError
    invalid = Header("Invalid Header", "value")  # Space not allowed
except ValidationError as e:
    print(f"Blocked: {e}")

# --- Duplicate Header Validation ---

# Strict mode (default) - no duplicates allowed except Set-Cookie
strict_headers = Headers(allow_duplicates=False)
strict_headers.add_raw("Content-Type", "application/json")

try:
    strict_headers.add_raw("Content-Type", "text/plain")  # Raises!
except ValidationError as e:
    print(f"Duplicate blocked: {e}")

# Lenient mode - duplicates allowed
lenient_headers = Headers(allow_duplicates=True)
lenient_headers.add_raw("X-Custom", "value1")
lenient_headers.add_raw("X-Custom", "value2")  # OK

# --- Manual Validation ---

# Validate header name
result: ValidationResult = RFC7230Validator.validate_field_name("Content-Type")
if result:
    print("Valid header name")
else:
    print(f"Invalid: {result.error}")

# Validate header value
result = RFC7230Validator.validate_field_value("application/json")

# Validate both name and value
result = RFC7230Validator.validate_header_field("Content-Type", "application/json")

# Validate header size (default max: 8192 bytes)
result = RFC7230Validator.validate_header_size(
    "X-Large-Header",
    "x" * 10000,
    max_size=8192
)

# Raise on error instead of returning ValidationResult
RFC7230Validator.validate_field_name("Content-Type", raise_on_error=True)
```

### 3. Authentication

Handle HTTP Basic and Bearer authentication safely.

```python
from pyhttp_util.auth import BasicAuth, BearerAuth
from pyhttp_util.headers import Header

# === Basic Authentication ===

# Encoding credentials (client side)
credentials = BasicAuth(login="username", password="secret123")
auth_value = credentials.encode()
print(auth_value)  # Basic dXNlcm5hbWU6c2VjcmV0MTIz

# Use as string directly
print(str(credentials))  # Basic dXNlcm5hbWU6c2VjcmV0MTIz

# Decoding credentials (server side)
received = "Basic dXNlcm5hbWU6c2VjcmV0MTIz"
decoded = BasicAuth.decode(received)
print(f"User: {decoded.login}")      # username
print(f"Password: {decoded.password}")  # secret123

# Decode from Header object
header = Header("Authorization", "Basic dXNlcm5hbWU6c2VjcmV0MTIz")
decoded = BasicAuth.decode(header)

# Custom encoding (default is latin1)
credentials = BasicAuth(login="user", password="пароль", encoding="utf-8")

# Validation: login cannot contain ":"
try:
    invalid = BasicAuth(login="user:name", password="pass")  # Raises!
except ValueError as e:
    print(f"Invalid: {e}")

# === Bearer Authentication ===

# Encoding token
token_auth = BearerAuth(token="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...")
auth_value = token_auth.encode()
print(auth_value)  # Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...

# Decoding token
received = "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
decoded = BearerAuth.decode(received)
print(f"Token: {decoded.token}")

# Validation: token cannot be empty or contain whitespace
try:
    invalid = BearerAuth(token="")  # Raises!
except ValueError as e:
    print(f"Invalid: {e}")
```

### 4. Cookies

Full RFC 6265 compliant cookie handling.

```python
from datetime import datetime, timezone, timedelta
from pyhttp_util.headers import Cookie, CookieJar, SameSite

# === Creating Cookies ===

# Simple session cookie
session = Cookie(name="session_id", value="abc123")

# Secure cookie with all attributes
secure_cookie = Cookie(
    name="auth_token",
    value="xyz789",
    domain=".example.com",
    path="/api",
    expires=datetime.now(timezone.utc) + timedelta(days=7), # or just provide seconds to expiration
    max_age=604800,  # 7 days in seconds
    secure=True,
    httponly=True,
    samesite=SameSite.STRICT,
    partitioned=False,
)

# SameSite options
Cookie(name="lax", value="1", samesite=SameSite.LAX)
Cookie(name="strict", value="1", samesite=SameSite.STRICT)
Cookie(name="none", value="1", samesite=SameSite.NONE, secure=True)  # Secure required!

# Convert to Set-Cookie header value
print(str(secure_cookie))
# auth_token=xyz789; Domain=.example.com; Path=/api; Expires=...; Max-Age=604800; Secure; HttpOnly; SameSite=Strict

# === Cookie Validation ===

try:
    # SameSite=None requires Secure
    invalid = Cookie(name="bad", value="1", samesite=SameSite.NONE, secure=False)
except Exception as e:
    print(f"Validation error: {e}")

# === Using CookieJar ===

jar = CookieJar()

# Add cookies
jar.add(Cookie(name="user_id", value="12345", domain=".example.com"))
jar.add(Cookie(name="prefs", value="dark_mode", path="/settings"))
jar.add(Cookie(
    name="temp",
    value="data",
    max_age=3600,  # expires is auto-calculated
))

# Filter cookies for a request
matching = jar.filter(
    domain="www.example.com",
    path="/settings/profile",
    secure=True,
)

# Get Cookie header value for request
cookie_header = jar.output(
    domain="www.example.com",
    path="/api/users",
    secure=True,
)
print(cookie_header)  # user_id=12345; prefs=dark_mode

# Remove a cookie
jar.discard(name="temp", domain=None, path="/")

# Clear all cookies
jar.clear()

# Iterate over cookies
for cookie in jar:
    print(f"{cookie.name}={cookie.value}")

# Count cookies
print(f"Total cookies: {len(jar)}")
```

### 5. Timeouts

Configure timeouts for HTTP clients with an immutable, validated structure.

```python
from pyhttp_util.timeout import Timeout

# === Creating Timeouts ===

# Simple total timeout
timeout = Timeout.create(total=30.0)

# Granular configuration
timeout = Timeout(
    total=60.0,       # Total operation timeout
    connect=5.0,      # Connection establishment timeout
    sock_connect=3.0, # Socket connection phase timeout
    sock_read=10.0,   # Socket read timeout
)

# All values are optional (None = no timeout)
timeout = Timeout(connect=5.0)  # Only connect timeout

# === Validation ===

# Negative values are not allowed
try:
    invalid = Timeout(total=-1.0)  # Raises ValueError!
except ValueError as e:
    print(f"Invalid: {e}")

# === Normalizing Different Timeout Types ===

# From int/float (becomes total timeout)
timeout = Timeout.normalize(30)      # Timeout(total=30)
timeout = Timeout.normalize(30.5)    # Timeout(total=30.5)

# From existing Timeout (returns as-is)
existing = Timeout(total=60.0)
timeout = Timeout.normalize(existing)  # Same object

# From any object with timeout attributes (duck typing)
class CustomTimeout:
    total = 30.0
    connect = 5.0
    sock_connect = None
    sock_read = 10.0

timeout = Timeout.normalize(CustomTimeout())

# === Immutability ===

timeout = Timeout(total=30.0)
# timeout.total = 60.0  # Raises FrozenInstanceError!

# Create a new timeout instead
new_timeout = Timeout(
    total=60.0,
    connect=timeout.connect,
    sock_connect=timeout.sock_connect,
    sock_read=timeout.sock_read,
)
```

## API Reference

### Headers Module

| Class | Description |
|-------|-------------|
| `Header` | Immutable dataclass representing a single HTTP header |
| `Headers` | Mutable collection of headers with case-insensitive lookups |
| `HTTPHeader` | Enum of 100+ standard HTTP header names |
| `HeaderBuilder` | Static factory methods for creating standard headers |
| `HeadersDict` | TypedDict for type-safe header dictionaries |

### Cookies Module

| Class | Description |
|-------|-------------|
| `Cookie` | Immutable dataclass representing an HTTP cookie |
| `CookieJar` | Container for managing multiple cookies |
| `SameSite` | Enum for SameSite attribute (`LAX`, `STRICT`, `NONE`) |

### Auth Module

| Class | Description |
|-------|-------------|
| `BasicAuth` | HTTP Basic Authentication encoding/decoding |
| `BearerAuth` | HTTP Bearer Token encoding/decoding |

### Timeout Module

| Class | Description |
|-------|-------------|
| `Timeout` | Immutable timeout configuration |

### Validator Module

| Class | Description |
|-------|-------------|
| `RFC7230Validator` | Static methods for RFC 7230 validation |
| `ValidationError` | Exception raised on validation failure |
| `ValidationResult` | Result object with `valid` and `error` attributes |

## Development

### Prerequisites

- Python 3.10+
- [uv](https://github.com/astral-sh/uv) (recommended) or pip

### Setup

```bash
# Clone the repository
git clone https://github.com/GrehBan/pyhttp-util.git
cd pyhttp-util

# Install dependencies
uv sync
```

### Running Linters

```bash
# Check code style
uv run ruff check .

# Format code
uv run ruff format .

# Type checking
uv run mypy pyhttp_util
```

## License

MIT License - see [LICENSE](LICENSE) for details.
