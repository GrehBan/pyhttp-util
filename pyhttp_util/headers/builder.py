"""Helper class for building HTTP headers.

RFC 9110: HTTP Semantics
https://datatracker.ietf.org/doc/html/rfc9110
"""

from __future__ import annotations

from pyhttp_util.headers.headers import Header
from pyhttp_util.headers.headers_enum import HTTPHeader

__all__ = ("HeaderBuilder",)


class HeaderBuilder:
    """Static factory methods for creating standard HTTP headers (RFC 9110)."""

    @staticmethod
    def authorization(value: str) -> Header:
        """Creates an Authorization header (RFC 9110)."""
        return Header(HTTPHeader.AUTHORIZATION, value)

    @staticmethod
    def proxy_authorization(value: str) -> Header:
        """Creates a Proxy-Authorization header (RFC 9110)."""
        return Header(HTTPHeader.PROXY_AUTHORIZATION, value)

    @staticmethod
    def www_authenticate(value: str) -> Header:
        """Creates a WWW-Authenticate header (RFC 9110)."""
        return Header(HTTPHeader.WWW_AUTHENTICATE, value)

    @staticmethod
    def proxy_authenticate(value: str) -> Header:
        """Creates a Proxy-Authenticate header (RFC 9110)."""
        return Header(HTTPHeader.PROXY_AUTHENTICATE, value)

    @staticmethod
    def age(value: str) -> Header:
        """Creates an Age header (RFC 9111)."""
        return Header(HTTPHeader.AGE, value)

    @staticmethod
    def cache_control(value: str) -> Header:
        """Creates a Cache-Control header (RFC 9111)."""
        return Header(HTTPHeader.CACHE_CONTROL, value)

    @staticmethod
    def clear_site_data(value: str) -> Header:
        """Creates a Clear-Site-Data header (W3C)."""
        return Header(HTTPHeader.CLEAR_SITE_DATA, value)

    @staticmethod
    def expires(value: str) -> Header:
        """Creates an Expires header (RFC 9111)."""
        return Header(HTTPHeader.EXPIRES, value)

    @staticmethod
    def pragma(value: str) -> Header:
        """Creates a Pragma header (RFC 9111)."""
        return Header(HTTPHeader.PRAGMA, value)

    @staticmethod
    def warning(value: str) -> Header:
        """Creates a Warning header (RFC 9111)."""
        return Header(HTTPHeader.WARNING, value)

    @staticmethod
    def accept_ch(value: str) -> Header:
        """Creates an Accept-CH header (RFC 8942)."""
        return Header(HTTPHeader.ACCEPT_CH, value)

    @staticmethod
    def accept_ch_lifetime(value: str) -> Header:
        """Creates an Accept-CH-Lifetime header."""
        return Header(HTTPHeader.ACCEPT_CH_LIFETIME, value)

    @staticmethod
    def sec_ch_ua(value: str) -> Header:
        """Creates a Sec-CH-UA header (RFC 8942)."""
        return Header(HTTPHeader.SEC_CH_UA, value)

    @staticmethod
    def sec_ch_ua_arch(value: str) -> Header:
        """Creates a Sec-CH-UA-Arch header (RFC 8942)."""
        return Header(HTTPHeader.SEC_CH_UA_ARCH, value)

    @staticmethod
    def sec_ch_ua_bitness(value: str) -> Header:
        """Creates a Sec-CH-UA-Bitness header (RFC 8942)."""
        return Header(HTTPHeader.SEC_CH_UA_BITNESS, value)

    @staticmethod
    def sec_ch_ua_full_version(value: str) -> Header:
        """Creates a Sec-CH-UA-Full-Version header (RFC 8942)."""
        return Header(HTTPHeader.SEC_CH_UA_FULL_VERSION, value)

    @staticmethod
    def sec_ch_ua_full_version_list(value: str) -> Header:
        """Creates a Sec-CH-UA-Full-Version-List header (RFC 8942)."""
        return Header(HTTPHeader.SEC_CH_UA_FULL_VERSION_LIST, value)

    @staticmethod
    def sec_ch_ua_mobile(value: str) -> Header:
        """Creates a Sec-CH-UA-Mobile header (RFC 8942)."""
        return Header(HTTPHeader.SEC_CH_UA_MOBILE, value)

    @staticmethod
    def sec_ch_ua_model(value: str) -> Header:
        """Creates a Sec-CH-UA-Model header (RFC 8942)."""
        return Header(HTTPHeader.SEC_CH_UA_MODEL, value)

    @staticmethod
    def sec_ch_ua_platform(value: str) -> Header:
        """Creates a Sec-CH-UA-Platform header (RFC 8942)."""
        return Header(HTTPHeader.SEC_CH_UA_PLATFORM, value)

    @staticmethod
    def sec_ch_ua_platform_version(value: str) -> Header:
        """Creates a Sec-CH-UA-Platform-Version header (RFC 8942)."""
        return Header(HTTPHeader.SEC_CH_UA_PLATFORM_VERSION, value)

    @staticmethod
    def sec_ch_ua_wow64(value: str) -> Header:
        """Creates a Sec-CH-UA-WoW64 header (RFC 8942)."""
        return Header(HTTPHeader.SEC_CH_UA_WOW64, value)

    @staticmethod
    def etag(value: str) -> Header:
        """Creates an ETag header (RFC 9110)."""
        return Header(HTTPHeader.ETAG, value)

    @staticmethod
    def if_match(value: str) -> Header:
        """Creates an If-Match header (RFC 9110)."""
        return Header(HTTPHeader.IF_MATCH, value)

    @staticmethod
    def if_modified_since(value: str) -> Header:
        """Creates an If-Modified-Since header (RFC 9110)."""
        return Header(HTTPHeader.IF_MODIFIED_SINCE, value)

    @staticmethod
    def if_none_match(value: str) -> Header:
        """Creates an If-None-Match header (RFC 9110)."""
        return Header(HTTPHeader.IF_NONE_MATCH, value)

    @staticmethod
    def if_unmodified_since(value: str) -> Header:
        """Creates an If-Unmodified-Since header (RFC 9110)."""
        return Header(HTTPHeader.IF_UNMODIFIED_SINCE, value)

    @staticmethod
    def last_modified(value: str) -> Header:
        """Creates a Last-Modified header (RFC 9110)."""
        return Header(HTTPHeader.LAST_MODIFIED, value)

    @staticmethod
    def vary(value: str) -> Header:
        """Creates a Vary header (RFC 9110)."""
        return Header(HTTPHeader.VARY, value)

    @staticmethod
    def connection(value: str) -> Header:
        """Creates a Connection header (RFC 9110)."""
        return Header(HTTPHeader.CONNECTION, value)

    @staticmethod
    def keep_alive(value: str) -> Header:
        """Creates a Keep-Alive header (RFC 9110)."""
        return Header(HTTPHeader.KEEP_ALIVE, value)

    @staticmethod
    def proxy_connection(value: str) -> Header:
        """Creates a Proxy-Connection header."""
        return Header(HTTPHeader.PROXY_CONNECTION, value)

    @staticmethod
    def te(value: str) -> Header:
        """Creates a TE header (RFC 9110)."""
        return Header(HTTPHeader.TE, value)

    @staticmethod
    def trailer(value: str) -> Header:
        """Creates a Trailer header (RFC 9110)."""
        return Header(HTTPHeader.TRAILER, value)

    @staticmethod
    def upgrade(value: str) -> Header:
        """Creates an Upgrade header (RFC 9110)."""
        return Header(HTTPHeader.UPGRADE, value)

    @staticmethod
    def cookie(value: str) -> Header:
        """Creates a Cookie header (RFC 6265)."""
        return Header(HTTPHeader.COOKIE, value)

    @staticmethod
    def set_cookie(value: str) -> Header:
        """Creates a Set-Cookie header (RFC 6265)."""
        return Header(HTTPHeader.SET_COOKIE, value)

    @staticmethod
    def accept(value: str) -> Header:
        """Creates an Accept header (RFC 9110)."""
        return Header(HTTPHeader.ACCEPT, value)

    @staticmethod
    def accept_charset(value: str) -> Header:
        """Creates an Accept-Charset header (RFC 9110)."""
        return Header(HTTPHeader.ACCEPT_CHARSET, value)

    @staticmethod
    def accept_encoding(value: str) -> Header:
        """Creates an Accept-Encoding header (RFC 9110)."""
        return Header(HTTPHeader.ACCEPT_ENCODING, value)

    @staticmethod
    def accept_language(value: str) -> Header:
        """Creates an Accept-Language header (RFC 9110)."""
        return Header(HTTPHeader.ACCEPT_LANGUAGE, value)

    @staticmethod
    def content_disposition(value: str) -> Header:
        """Creates a Content-Disposition header (RFC 6266)."""
        return Header(HTTPHeader.CONTENT_DISPOSITION, value)

    @staticmethod
    def content_encoding(value: str) -> Header:
        """Creates a Content-Encoding header (RFC 9110)."""
        return Header(HTTPHeader.CONTENT_ENCODING, value)

    @staticmethod
    def content_language(value: str) -> Header:
        """Creates a Content-Language header (RFC 9110)."""
        return Header(HTTPHeader.CONTENT_LANGUAGE, value)

    @staticmethod
    def content_length(value: str) -> Header:
        """Creates a Content-Length header (RFC 9110)."""
        return Header(HTTPHeader.CONTENT_LENGTH, value)

    @staticmethod
    def content_location(value: str) -> Header:
        """Creates a Content-Location header (RFC 9110)."""
        return Header(HTTPHeader.CONTENT_LOCATION, value)

    @staticmethod
    def content_type(value: str) -> Header:
        """Creates a Content-Type header (RFC 9110)."""
        return Header(HTTPHeader.CONTENT_TYPE, value)

    @staticmethod
    def expect(value: str) -> Header:
        """Creates an Expect header (RFC 9110)."""
        return Header(HTTPHeader.EXPECT, value)

    @staticmethod
    def max_forwards(value: str) -> Header:
        """Creates a Max-Forwards header (RFC 9110)."""
        return Header(HTTPHeader.MAX_FORWARDS, value)

    @staticmethod
    def accept_ranges(value: str) -> Header:
        """Creates an Accept-Ranges header (RFC 9110)."""
        return Header(HTTPHeader.ACCEPT_RANGES, value)

    @staticmethod
    def content_range(value: str) -> Header:
        """Creates a Content-Range header (RFC 9110)."""
        return Header(HTTPHeader.CONTENT_RANGE, value)

    @staticmethod
    def if_range(value: str) -> Header:
        """Creates an If-Range header (RFC 9110)."""
        return Header(HTTPHeader.IF_RANGE, value)

    @staticmethod
    def range(value: str) -> Header:
        """Creates a Range header (RFC 9110)."""
        return Header(HTTPHeader.RANGE, value)

    @staticmethod
    def transfer_encoding(value: str) -> Header:
        """Creates a Transfer-Encoding header (RFC 9110)."""
        return Header(HTTPHeader.TRANSFER_ENCODING, value)

    @staticmethod
    def forwarded(value: str) -> Header:
        """Creates a Forwarded header (RFC 7239)."""
        return Header(HTTPHeader.FORWARDED, value)

    @staticmethod
    def via(value: str) -> Header:
        """Creates a Via header (RFC 9110)."""
        return Header(HTTPHeader.VIA, value)

    @staticmethod
    def x_forwarded_for(value: str) -> Header:
        """Creates an X-Forwarded-For header."""
        return Header(HTTPHeader.X_FORWARDED_FOR, value)

    @staticmethod
    def x_forwarded_host(value: str) -> Header:
        """Creates an X-Forwarded-Host header."""
        return Header(HTTPHeader.X_FORWARDED_HOST, value)

    @staticmethod
    def x_forwarded_proto(value: str) -> Header:
        """Creates an X-Forwarded-Proto header."""
        return Header(HTTPHeader.X_FORWARDED_PROTO, value)

    @staticmethod
    def x_via(value: str) -> Header:
        """Creates an X-Via header."""
        return Header(HTTPHeader.X_VIA, value)

    @staticmethod
    def location(value: str) -> Header:
        """Creates a Location header (RFC 9110)."""
        return Header(HTTPHeader.LOCATION, value)

    @staticmethod
    def refresh(value: str) -> Header:
        """Creates a Refresh header."""
        return Header(HTTPHeader.REFRESH, value)

    @staticmethod
    def from_(value: str) -> Header:
        """Creates a From header (RFC 9110)."""
        return Header(HTTPHeader.FROM, value)

    @staticmethod
    def host(value: str) -> Header:
        """Creates a Host header (RFC 9110)."""
        return Header(HTTPHeader.HOST, value)

    @staticmethod
    def referer(value: str) -> Header:
        """Creates a Referer header (RFC 9110)."""
        return Header(HTTPHeader.REFERER, value)

    @staticmethod
    def referrer_policy(value: str) -> Header:
        """Creates a Referrer-Policy header (W3C)."""
        return Header(HTTPHeader.REFERRER_POLICY, value)

    @staticmethod
    def user_agent(value: str) -> Header:
        """Creates a User-Agent header (RFC 9110)."""
        return Header(HTTPHeader.USER_AGENT, value)

    @staticmethod
    def allow(value: str) -> Header:
        """Creates an Allow header (RFC 9110)."""
        return Header(HTTPHeader.ALLOW, value)

    @staticmethod
    def server(value: str) -> Header:
        """Creates a Server header (RFC 9110)."""
        return Header(HTTPHeader.SERVER, value)

    @staticmethod
    def content_security_policy(value: str) -> Header:
        """Creates a Content-Security-Policy header (W3C)."""
        return Header(HTTPHeader.CONTENT_SECURITY_POLICY, value)

    @staticmethod
    def content_security_policy_report_only(value: str) -> Header:
        """Creates a Content-Security-Policy-Report-Only header (W3C)."""
        return Header(HTTPHeader.CONTENT_SECURITY_POLICY_REPORT_ONLY, value)

    @staticmethod
    def cross_origin_embedder_policy(value: str) -> Header:
        """Creates a Cross-Origin-Embedder-Policy header (W3C)."""
        return Header(HTTPHeader.CROSS_ORIGIN_EMBEDDER_POLICY, value)

    @staticmethod
    def cross_origin_opener_policy(value: str) -> Header:
        """Creates a Cross-Origin-Opener-Policy header (W3C)."""
        return Header(HTTPHeader.CROSS_ORIGIN_OPENER_POLICY, value)

    @staticmethod
    def cross_origin_resource_policy(value: str) -> Header:
        """Creates a Cross-Origin-Resource-Policy header (W3C)."""
        return Header(HTTPHeader.CROSS_ORIGIN_RESOURCE_POLICY, value)

    @staticmethod
    def expect_ct(value: str) -> Header:
        """Creates an Expect-CT header."""
        return Header(HTTPHeader.EXPECT_CT, value)

    @staticmethod
    def feature_policy(value: str) -> Header:
        """Creates a Feature-Policy header (W3C)."""
        return Header(HTTPHeader.FEATURE_POLICY, value)

    @staticmethod
    def permissions_policy(value: str) -> Header:
        """Creates a Permissions-Policy header (W3C)."""
        return Header(HTTPHeader.PERMISSIONS_POLICY, value)

    @staticmethod
    def strict_transport_security(value: str) -> Header:
        """Creates a Strict-Transport-Security header (RFC 6797)."""
        return Header(HTTPHeader.STRICT_TRANSPORT_SECURITY, value)

    @staticmethod
    def upgrade_insecure_requests(value: str) -> Header:
        """Creates an Upgrade-Insecure-Requests header (W3C)."""
        return Header(HTTPHeader.UPGRADE_INSECURE_REQUESTS, value)

    @staticmethod
    def x_content_type_options(value: str) -> Header:
        """Creates an X-Content-Type-Options header."""
        return Header(HTTPHeader.X_CONTENT_TYPE_OPTIONS, value)

    @staticmethod
    def x_download_options(value: str) -> Header:
        """Creates an X-Download-Options header."""
        return Header(HTTPHeader.X_DOWNLOAD_OPTIONS, value)

    @staticmethod
    def x_frame_options(value: str) -> Header:
        """Creates an X-Frame-Options header (RFC 7034)."""
        return Header(HTTPHeader.X_FRAME_OPTIONS, value)

    @staticmethod
    def x_permitted_cross_domain_policies(value: str) -> Header:
        """Creates an X-Permitted-Cross-Domain-Policies header."""
        return Header(HTTPHeader.X_PERMITTED_CROSS_DOMAIN_POLICIES, value)

    @staticmethod
    def x_powered_by(value: str) -> Header:
        """Creates an X-Powered-By header."""
        return Header(HTTPHeader.X_POWERED_BY, value)

    @staticmethod
    def x_xss_protection(value: str) -> Header:
        """Creates an X-XSS-Protection header."""
        return Header(HTTPHeader.X_XSS_PROTECTION, value)

    @staticmethod
    def access_control_allow_credentials(value: str) -> Header:
        """Creates an Access-Control-Allow-Credentials header (W3C)."""
        return Header(HTTPHeader.ACCESS_CONTROL_ALLOW_CREDENTIALS, value)

    @staticmethod
    def access_control_allow_headers(value: str) -> Header:
        """Creates an Access-Control-Allow-Headers header (W3C)."""
        return Header(HTTPHeader.ACCESS_CONTROL_ALLOW_HEADERS, value)

    @staticmethod
    def access_control_allow_methods(value: str) -> Header:
        """Creates an Access-Control-Allow-Methods header (W3C)."""
        return Header(HTTPHeader.ACCESS_CONTROL_ALLOW_METHODS, value)

    @staticmethod
    def access_control_allow_origin(value: str) -> Header:
        """Creates an Access-Control-Allow-Origin header (W3C)."""
        return Header(HTTPHeader.ACCESS_CONTROL_ALLOW_ORIGIN, value)

    @staticmethod
    def access_control_expose_headers(value: str) -> Header:
        """Creates an Access-Control-Expose-Headers header (W3C)."""
        return Header(HTTPHeader.ACCESS_CONTROL_EXPOSE_HEADERS, value)

    @staticmethod
    def access_control_max_age(value: str) -> Header:
        """Creates an Access-Control-Max-Age header (W3C)."""
        return Header(HTTPHeader.ACCESS_CONTROL_MAX_AGE, value)

    @staticmethod
    def access_control_request_headers(value: str) -> Header:
        """Creates an Access-Control-Request-Headers header (W3C)."""
        return Header(HTTPHeader.ACCESS_CONTROL_REQUEST_HEADERS, value)

    @staticmethod
    def access_control_request_method(value: str) -> Header:
        """Creates an Access-Control-Request-Method header (W3C)."""
        return Header(HTTPHeader.ACCESS_CONTROL_REQUEST_METHOD, value)

    @staticmethod
    def origin(value: str) -> Header:
        """Creates an Origin header (RFC 6454)."""
        return Header(HTTPHeader.ORIGIN, value)

    @staticmethod
    def timing_allow_origin(value: str) -> Header:
        """Creates a Timing-Allow-Origin header (W3C)."""
        return Header(HTTPHeader.TIMING_ALLOW_ORIGIN, value)

    @staticmethod
    def last_event_id(value: str) -> Header:
        """Creates a Last-Event-ID header (W3C)."""
        return Header(HTTPHeader.LAST_EVENT_ID, value)

    @staticmethod
    def nel(value: str) -> Header:
        """Creates a NEL header (W3C)."""
        return Header(HTTPHeader.NEL, value)

    @staticmethod
    def ping_from(value: str) -> Header:
        """Creates a Ping-From header."""
        return Header(HTTPHeader.PING_FROM, value)

    @staticmethod
    def ping_to(value: str) -> Header:
        """Creates a Ping-To header."""
        return Header(HTTPHeader.PING_TO, value)

    @staticmethod
    def report_to(value: str) -> Header:
        """Creates a Report-To header (W3C)."""
        return Header(HTTPHeader.REPORT_TO, value)

    @staticmethod
    def server_timing(value: str) -> Header:
        """Creates a Server-Timing header (W3C)."""
        return Header(HTTPHeader.SERVER_TIMING, value)

    @staticmethod
    def sec_websocket_accept(value: str) -> Header:
        """Creates a Sec-WebSocket-Accept header (RFC 6455)."""
        return Header(HTTPHeader.SEC_WEBSOCKET_ACCEPT, value)

    @staticmethod
    def sec_websocket_extensions(value: str) -> Header:
        """Creates a Sec-WebSocket-Extensions header (RFC 6455)."""
        return Header(HTTPHeader.SEC_WEBSOCKET_EXTENSIONS, value)

    @staticmethod
    def sec_websocket_key(value: str) -> Header:
        """Creates a Sec-WebSocket-Key header (RFC 6455)."""
        return Header(HTTPHeader.SEC_WEBSOCKET_KEY, value)

    @staticmethod
    def sec_websocket_protocol(value: str) -> Header:
        """Creates a Sec-WebSocket-Protocol header (RFC 6455)."""
        return Header(HTTPHeader.SEC_WEBSOCKET_PROTOCOL, value)

    @staticmethod
    def sec_websocket_version(value: str) -> Header:
        """Creates a Sec-WebSocket-Version header (RFC 6455)."""
        return Header(HTTPHeader.SEC_WEBSOCKET_VERSION, value)

    @staticmethod
    def accept_patch(value: str) -> Header:
        """Creates an Accept-Patch header (RFC 5789)."""
        return Header(HTTPHeader.ACCEPT_PATCH, value)

    @staticmethod
    def accept_post(value: str) -> Header:
        """Creates an Accept-Post header (W3C)."""
        return Header(HTTPHeader.ACCEPT_POST, value)

    @staticmethod
    def accept_push_policy(value: str) -> Header:
        """Creates an Accept-Push-Policy header."""
        return Header(HTTPHeader.ACCEPT_PUSH_POLICY, value)

    @staticmethod
    def accept_signature(value: str) -> Header:
        """Creates an Accept-Signature header."""
        return Header(HTTPHeader.ACCEPT_SIGNATURE, value)

    @staticmethod
    def alt_svc(value: str) -> Header:
        """Creates an Alt-Svc header (RFC 7838)."""
        return Header(HTTPHeader.ALT_SVC, value)

    @staticmethod
    def date(value: str) -> Header:
        """Creates a Date header (RFC 9110)."""
        return Header(HTTPHeader.DATE, value)

    @staticmethod
    def early_data(value: str) -> Header:
        """Creates an Early-Data header (RFC 8470)."""
        return Header(HTTPHeader.EARLY_DATA, value)

    @staticmethod
    def large_allocation(value: str) -> Header:
        """Creates a Large-Allocation header."""
        return Header(HTTPHeader.LARGE_ALLOCATION, value)

    @staticmethod
    def link(value: str) -> Header:
        """Creates a Link header (RFC 8288)."""
        return Header(HTTPHeader.LINK, value)

    @staticmethod
    def push_policy(value: str) -> Header:
        """Creates a Push-Policy header."""
        return Header(HTTPHeader.PUSH_POLICY, value)

    @staticmethod
    def retry_after(value: str) -> Header:
        """Creates a Retry-After header (RFC 9110)."""
        return Header(HTTPHeader.RETRY_AFTER, value)

    @staticmethod
    def save_data(value: str) -> Header:
        """Creates a Save-Data header (W3C)."""
        return Header(HTTPHeader.SAVE_DATA, value)

    @staticmethod
    def sec_fetch_dest(value: str) -> Header:
        """Creates a Sec-Fetch-Dest header (W3C)."""
        return Header(HTTPHeader.SEC_FETCH_DEST, value)

    @staticmethod
    def sec_fetch_mode(value: str) -> Header:
        """Creates a Sec-Fetch-Mode header (W3C)."""
        return Header(HTTPHeader.SEC_FETCH_MODE, value)

    @staticmethod
    def sec_fetch_site(value: str) -> Header:
        """Creates a Sec-Fetch-Site header (W3C)."""
        return Header(HTTPHeader.SEC_FETCH_SITE, value)

    @staticmethod
    def sec_fetch_user(value: str) -> Header:
        """Creates a Sec-Fetch-User header (W3C)."""
        return Header(HTTPHeader.SEC_FETCH_USER, value)

    @staticmethod
    def service_worker_navigation_preload(value: str) -> Header:
        """Creates a Service-Worker-Navigation-Preload header (W3C)."""
        return Header(HTTPHeader.SERVICE_WORKER_NAVIGATION_PRELOAD, value)

    @staticmethod
    def signature(value: str) -> Header:
        """Creates a Signature header."""
        return Header(HTTPHeader.SIGNATURE, value)

    @staticmethod
    def signed_headers(value: str) -> Header:
        """Creates a Signed-Headers header."""
        return Header(HTTPHeader.SIGNED_HEADERS, value)

    @staticmethod
    def sourcemap(value: str) -> Header:
        """Creates a SourceMap header."""
        return Header(HTTPHeader.SOURCEMAP, value)

    @staticmethod
    def x_dns_prefetch_control(value: str) -> Header:
        """Creates an X-DNS-Prefetch-Control header."""
        return Header(HTTPHeader.X_DNS_PREFETCH_CONTROL, value)

    @staticmethod
    def x_firefox_spdy(value: str) -> Header:
        """Creates an X-Firefox-Spdy header."""
        return Header(HTTPHeader.X_FIREFOX_SPDY, value)

    @staticmethod
    def x_pingback(value: str) -> Header:
        """Creates an X-Pingback header."""
        return Header(HTTPHeader.X_PINGBACK, value)

    @staticmethod
    def x_requested_with(value: str) -> Header:
        """Creates an X-Requested-With header."""
        return Header(HTTPHeader.X_REQUESTED_WITH, value)

    @staticmethod
    def x_robots_tag(value: str) -> Header:
        """Creates an X-Robots-Tag header."""
        return Header(HTTPHeader.X_ROBOTS_TAG, value)

    @staticmethod
    def x_ua_compatible(value: str) -> Header:
        """Creates an X-UA-Compatible header."""
        return Header(HTTPHeader.X_UA_COMPATIBLE, value)