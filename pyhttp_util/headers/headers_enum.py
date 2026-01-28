"""Enumeration of standard HTTP headers.

RFC 9110: HTTP Semantics
https://datatracker.ietf.org/doc/html/rfc9110
"""

from enum import Enum

from multidict import istr

__all__ = ("HTTPHeader",)


class HTTPHeader(str, Enum):
    """Comprehensive HTTP headers enumeration (RFC 9110, RFC 6265, etc.).

    This enumeration contains standard HTTP headers defined in RFCs.
    The values are wrapped in `multidict.istr` for case-insensitive comparison.
    """

    AUTHORIZATION = istr("Authorization")
    PROXY_AUTHORIZATION = istr("Proxy-Authorization")
    WWW_AUTHENTICATE = istr("WWW-Authenticate")
    PROXY_AUTHENTICATE = istr("Proxy-Authenticate")

    AGE = istr("Age")
    CACHE_CONTROL = istr("Cache-Control")
    CLEAR_SITE_DATA = istr("Clear-Site-Data")
    EXPIRES = istr("Expires")
    PRAGMA = istr("Pragma")
    WARNING = istr("Warning")

    ACCEPT_CH = istr("Accept-CH")
    ACCEPT_CH_LIFETIME = istr("Accept-CH-Lifetime")
    SEC_CH_UA = istr("Sec-CH-UA")
    SEC_CH_UA_ARCH = istr("Sec-CH-UA-Arch")
    SEC_CH_UA_BITNESS = istr("Sec-CH-UA-Bitness")
    SEC_CH_UA_FULL_VERSION = istr("Sec-CH-UA-Full-Version")
    SEC_CH_UA_FULL_VERSION_LIST = istr("Sec-CH-UA-Full-Version-List")
    SEC_CH_UA_MOBILE = istr("Sec-CH-UA-Mobile")
    SEC_CH_UA_MODEL = istr("Sec-CH-UA-Model")
    SEC_CH_UA_PLATFORM = istr("Sec-CH-UA-Platform")
    SEC_CH_UA_PLATFORM_VERSION = istr("Sec-CH-UA-Platform-Version")
    SEC_CH_UA_WOW64 = istr("Sec-CH-UA-WoW64")

    ETAG = istr("ETag")
    IF_MATCH = istr("If-Match")
    IF_MODIFIED_SINCE = istr("If-Modified-Since")
    IF_NONE_MATCH = istr("If-None-Match")
    IF_UNMODIFIED_SINCE = istr("If-Unmodified-Since")
    LAST_MODIFIED = istr("Last-Modified")
    VARY = istr("Vary")

    CONNECTION = istr("Connection")
    KEEP_ALIVE = istr("Keep-Alive")
    PROXY_CONNECTION = istr("Proxy-Connection")
    TE = istr("TE")
    TRAILER = istr("Trailer")
    UPGRADE = istr("Upgrade")

    COOKIE = istr("Cookie")
    SET_COOKIE = istr("Set-Cookie")

    ACCEPT = istr("Accept")
    ACCEPT_CHARSET = istr("Accept-Charset")
    ACCEPT_ENCODING = istr("Accept-Encoding")
    ACCEPT_LANGUAGE = istr("Accept-Language")

    CONTENT_DISPOSITION = istr("Content-Disposition")
    CONTENT_ENCODING = istr("Content-Encoding")
    CONTENT_LANGUAGE = istr("Content-Language")
    CONTENT_LENGTH = istr("Content-Length")
    CONTENT_LOCATION = istr("Content-Location")
    CONTENT_TYPE = istr("Content-Type")

    EXPECT = istr("Expect")
    MAX_FORWARDS = istr("Max-Forwards")

    ACCEPT_RANGES = istr("Accept-Ranges")
    CONTENT_RANGE = istr("Content-Range")
    IF_RANGE = istr("If-Range")
    RANGE = istr("Range")

    TRANSFER_ENCODING = istr("Transfer-Encoding")

    FORWARDED = istr("Forwarded")
    VIA = istr("Via")
    X_FORWARDED_FOR = istr("X-Forwarded-For")
    X_FORWARDED_HOST = istr("X-Forwarded-Host")
    X_FORWARDED_PROTO = istr("X-Forwarded-Proto")
    X_VIA = istr("X-Via")

    LOCATION = istr("Location")
    REFRESH = istr("Refresh")

    FROM = istr("From")
    HOST = istr("Host")
    REFERER = istr("Referer")
    REFERRER_POLICY = istr("Referrer-Policy")
    USER_AGENT = istr("User-Agent")

    ALLOW = istr("Allow")
    SERVER = istr("Server")

    CONTENT_SECURITY_POLICY = istr("Content-Security-Policy")
    CONTENT_SECURITY_POLICY_REPORT_ONLY = istr(
        "Content-Security-Policy-Report-Only"
    )
    CROSS_ORIGIN_EMBEDDER_POLICY = istr("Cross-Origin-Embedder-Policy")
    CROSS_ORIGIN_OPENER_POLICY = istr("Cross-Origin-Opener-Policy")
    CROSS_ORIGIN_RESOURCE_POLICY = istr("Cross-Origin-Resource-Policy")
    EXPECT_CT = istr("Expect-CT")
    FEATURE_POLICY = istr("Feature-Policy")
    PERMISSIONS_POLICY = istr("Permissions-Policy")
    STRICT_TRANSPORT_SECURITY = istr("Strict-Transport-Security")
    UPGRADE_INSECURE_REQUESTS = istr("Upgrade-Insecure-Requests")
    X_CONTENT_TYPE_OPTIONS = istr("X-Content-Type-Options")
    X_DOWNLOAD_OPTIONS = istr("X-Download-Options")
    X_FRAME_OPTIONS = istr("X-Frame-Options")
    X_PERMITTED_CROSS_DOMAIN_POLICIES = istr(
        "X-Permitted-Cross-Domain-Policies"
    )
    X_POWERED_BY = istr("X-Powered-By")
    X_XSS_PROTECTION = istr("X-XSS-Protection")

    ACCESS_CONTROL_ALLOW_CREDENTIALS = istr("Access-Control-Allow-Credentials")
    ACCESS_CONTROL_ALLOW_HEADERS = istr("Access-Control-Allow-Headers")
    ACCESS_CONTROL_ALLOW_METHODS = istr("Access-Control-Allow-Methods")
    ACCESS_CONTROL_ALLOW_ORIGIN = istr("Access-Control-Allow-Origin")
    ACCESS_CONTROL_EXPOSE_HEADERS = istr("Access-Control-Expose-Headers")
    ACCESS_CONTROL_MAX_AGE = istr("Access-Control-Max-Age")
    ACCESS_CONTROL_REQUEST_HEADERS = istr("Access-Control-Request-Headers")
    ACCESS_CONTROL_REQUEST_METHOD = istr("Access-Control-Request-Method")
    ORIGIN = istr("Origin")
    TIMING_ALLOW_ORIGIN = istr("Timing-Allow-Origin")

    LAST_EVENT_ID = istr("Last-Event-ID")
    NEL = istr("NEL")
    PING_FROM = istr("Ping-From")
    PING_TO = istr("Ping-To")
    REPORT_TO = istr("Report-To")
    SERVER_TIMING = istr("Server-Timing")

    SEC_WEBSOCKET_ACCEPT = istr("Sec-WebSocket-Accept")
    SEC_WEBSOCKET_EXTENSIONS = istr("Sec-WebSocket-Extensions")
    SEC_WEBSOCKET_KEY = istr("Sec-WebSocket-Key")
    SEC_WEBSOCKET_PROTOCOL = istr("Sec-WebSocket-Protocol")
    SEC_WEBSOCKET_VERSION = istr("Sec-WebSocket-Version")

    ACCEPT_PATCH = istr("Accept-Patch")
    ACCEPT_POST = istr("Accept-Post")
    ACCEPT_PUSH_POLICY = istr("Accept-Push-Policy")
    ACCEPT_SIGNATURE = istr("Accept-Signature")
    ALT_SVC = istr("Alt-Svc")
    DATE = istr("Date")
    EARLY_DATA = istr("Early-Data")
    LARGE_ALLOCATION = istr("Large-Allocation")
    LINK = istr("Link")
    PUSH_POLICY = istr("Push-Policy")
    RETRY_AFTER = istr("Retry-After")
    SAVE_DATA = istr("Save-Data")
    SEC_FETCH_DEST = istr("Sec-Fetch-Dest")
    SEC_FETCH_MODE = istr("Sec-Fetch-Mode")
    SEC_FETCH_SITE = istr("Sec-Fetch-Site")
    SEC_FETCH_USER = istr("Sec-Fetch-User")
    SERVICE_WORKER_NAVIGATION_PRELOAD = istr(
        "Service-Worker-Navigation-Preload"
    )
    SIGNATURE = istr("Signature")
    SIGNED_HEADERS = istr("Signed-Headers")
    SOURCEMAP = istr("SourceMap")
    X_DNS_PREFETCH_CONTROL = istr("X-DNS-Prefetch-Control")
    X_FIREFOX_SPDY = istr("X-Firefox-Spdy")
    X_PINGBACK = istr("X-Pingback")
    X_REQUESTED_WITH = istr("X-Requested-With")
    X_ROBOTS_TAG = istr("X-Robots-Tag")
    X_UA_COMPATIBLE = istr("X-UA-Compatible")
