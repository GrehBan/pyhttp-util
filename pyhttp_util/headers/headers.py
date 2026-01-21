"Core header data structures."

from dataclasses import dataclass, field
from typing import Mapping, TypeAlias, MutableMapping, Union

from multidict import CIMultiDict, istr, CIMultiDictProxy, MultiDict, MultiDictProxy

from pyhttp_util.headers.headers_enum import HTTPHeader
from pyhttp_util.headers.headers_dict import HeadersDict
from pyhttp_util.headers.validator import RFC7230Validator, ValidationError

__all__ = ("Header", "Headers")

HeadersType: TypeAlias = (
    Mapping[str | istr, str]
    | CIMultiDict[str | istr, str]
    | CIMultiDictProxy[str | istr, str]
    | MultiDict[str | istr, str]
    | MultiDictProxy[str | istr, str]
    | MutableMapping[str | istr, str]
    | HeadersDict
)
HeaderName: TypeAlias = Union[HTTPHeader, istr, str]
HeaderType: TypeAlias = Union[str, "Header"]
validator = RFC7230Validator()

# Create a map for case-insensitive lookup of HTTPHeader members
_HEADER_NAME_MAP = {h.value.lower(): h for h in HTTPHeader}


def _ensure_header_name(name: HeaderName) -> HTTPHeader | istr:
    """Ensures header name is HTTPHeader or istr."""
    if isinstance(name, HTTPHeader):
        return name
    
    name_str = str(name)
    # Try case-insensitive lookup to find the canonical HTTPHeader
    if name_str.lower() in _HEADER_NAME_MAP:
        return _HEADER_NAME_MAP[name_str.lower()]
        
    try:
        return HTTPHeader(name)
    except ValueError:
        return istr(name)


@dataclass(frozen=True, slots=True)
class Header:
    """Represents a single HTTP header. 
    
    Attributes:
        name: The header name (HTTPHeader enum or istr).
        value: The header value string.
    """
    name: HTTPHeader | istr
    value: str

    def __post_init__(self) -> None:
        """Validates the header upon initialization."""
        validator.validate_header_field(str(self.name), self.value, raise_on_error=True)
        validator.validate_header_size(str(self.name), self.value, raise_on_error=True)

    def __str__(self) -> str:
        """Returns the string representation of the header (Name: Value)."""
        return f"{self.name}: {self.value}"
    
    def __repr__(self) -> str:
        """Returns the official string representation."""
        return f"Header({self.name!r}, {self.value!r})"

    def to_tuple(self) -> tuple[HTTPHeader | istr, str]:
        """Converts the header to a tuple. 
        
        Returns:
            A tuple of (name, value).
        """
        return (self.name, self.value)
    
    def to_dict(self) -> dict[HTTPHeader | istr, str]:
        """Converts the header to a dictionary. 
        
        Returns:
            A dictionary with a single item {name: value}.
        """
        return {self.name: self.value}
    
    def copy(self) -> "Header":
        """Creates a copy of the header. 
        
        Returns:
            A new Header instance.
        """
        return Header(self.name, self.value)

    @classmethod
    def build(cls, name: HeaderName, value: str) -> "Header":
        """Builds a Header instance, converting string names to HTTPHeader if possible. 
        
        Args:
            name: The header name.
            value: The header value.
            
        Returns:
            A new Header instance.
        """
        return cls(_ensure_header_name(name), value)


@dataclass
class Headers:
    """A collection of HTTP headers. 
    
    Maintains insertion order and allows case-insensitive lookups.
    Enforces RFC 7230 validation rules.
    
    Attributes:
        headers: List of Header objects maintaining order.
        headers_map: Case-insensitive map for fast lookups.
        allow_duplicates: Whether to bypass strict duplicate checking (default False).
    """
    headers: list[Header] = field(default_factory=list)
    headers_map: CIMultiDict[str | istr] = field(default_factory=CIMultiDict)
    allow_duplicates: bool = False

    def __post_init__(self) -> None:
        """Validates the collection upon initialization."""
        for header in self.headers:
            self.headers_map.add(header.name, header.value)
        
        if not self.allow_duplicates:
            validator.validate_no_duplicate_headers(
                [(str(h.name), h.value) for h in self.headers],
                raise_on_error=True
            )

    def add(self, header: Header) -> None:
        """Adds a Header object to the collection. 
        
        Args:
            header: The Header object to add.
            
        Raises:
            ValidationError: If adding this header violates duplicate rules.
        """
        name_lower = header.name.lower()
        if not self.allow_duplicates and name_lower in self.headers_map:
            if name_lower not in RFC7230Validator.ALLOWED_DUPLICATES:
                if name_lower in RFC7230Validator.COMMA_SEPARATED_HEADERS:
                    raise ValidationError(f"Duplicate header '{header.name}' should be combined with comma separation instead of multiple header fields")
                raise ValidationError(f"Duplicate header field not allowed: '{header.name}'")

        self.headers.append(header)
        self.headers_map.add(header.name, header.value)

    def add_raw(self, name: HeaderName, value: str) -> None:
        """Adds a header from raw name and value strings. 
        
        Args:
            name: The header name.
            value: The header value.
        """
        header = Header.build(name, value)
        self.add(header)

    def get(self, name: HeaderName) -> str | None:
        """Retrieves a header value by name. 
        
        Args:
            name: The header name. 
            
        Returns:
            The header value if found, else None.
        """
        return self.headers_map.get(_ensure_header_name(name))

    def get_all(self, name: HeaderName) -> list[str]:
        """Retrieves all values for a given header name. 
        
        Args:
            name: The header name.
            
        Returns:
            A list of header values.
        """
        return self.headers_map.getall(_ensure_header_name(name))
    
    def remove(self, name: HeaderName) -> None:
        """Removes all headers with the given name. 
        
        Args:
            name: The header name.
        """
        name = _ensure_header_name(name)
        self.headers = [h for h in self.headers if h.name != name]
        if name in self.headers_map:
            del self.headers_map[name]
    
    def clear(self) -> None:
        """Removes all headers."""
        self.headers.clear()
        self.headers_map.clear()
    
    def to_dict(self) -> CIMultiDict[str | istr]:
        """Returns a copy of the internal map. 
        
        Returns:
            A CIMultiDict containing the headers.
        """
        return self.headers_map.copy()
    
    def to_list(self) -> list[Header]:
        """Returns a copy of the internal list. 
        
        Returns:
            A list of Header objects.
        """
        return self.headers.copy()
    
    def to_tuples(self) -> list[tuple[HTTPHeader | istr, str]]:
        """Returns a list of tuples. 
        
        Returns:
            A list of (name, value) tuples.
        """
        return [header.to_tuple() for header in self.headers]
    
    def __contains__(self, name: HeaderName) -> bool:
        """Checks if a header exists. 
        
        Args:
            name: The header name.
            
        Returns:
            True if exists, False otherwise.
        """
        return _ensure_header_name(name) in self.headers_map
    
    def __len__(self) -> int:
        """Returns the number of headers. 
        
        Returns:
            The count of headers.
        """
        return len(self.headers)
    
    def __iter__(self):
        """Iterates over the headers. 
        
        Returns:
            An iterator over Header objects.
        """
        return iter(self.headers)
    
    def __getitem__(self, name: HeaderName) -> str:
        """Retrieves a header value via subscript. 
        
        Args:
            name: The header name.
            
        Returns:
            The header value.
            
        Raises:
            KeyError: If not found.
        """
        return self.headers_map[_ensure_header_name(name)]
    
    def __setitem__(self, name: HeaderName, value: str) -> None:
        """Sets a header value via subscript (replaces existing). 
        
        Args:
            name: The header name.
            value: The header value.
        """
        name = _ensure_header_name(name)
        self.remove(name)
        self.add_raw(name, value)
    
    def __delitem__(self, name: HeaderName) -> None:
        """Deletes a header via subscript. 
        
        Args:
            name: The header name.
        """
        self.remove(name)
    
    def __str__(self) -> str:
        """Returns string representation (headers separated by newlines)."""
        return "\n".join(str(h) for h in self.headers)
    
    def __repr__(self) -> str:
        """Returns official string representation."""
        return f"Headers({self.headers!r})"
    
    def copy(self) -> "Headers":
        """Creates a shallow copy. 
        
        Returns:
            A new Headers instance.
        """
        return Headers(self.to_list())
    
    def extend(self, other: "Headers") -> None:
        """Extends with headers from another collection. 
        
        Args:
            other: Another Headers object.
        """
        for header in other:
            self.add(header)
    
    def update(self, other: "Headers") -> None:
        """Replaces current headers with those from another collection. 
        
        Args:
            other: Another Headers object.
        """
        self.clear()
        self.extend(other)
    
    def merge(self, other: "Headers") -> None:
        """Merges headers, keeping existing ones if present. 
        
        Args:
            other: Another Headers object.
        """
        for header in other:
            if header.name not in self.headers_map:
                self.add(header)
    
    def items(self):
        """Returns items from the map. 
        
        Returns:
            Items view of the internal map.
        """
        return self.headers_map.items()
    
    def keys(self):
        """Returns keys from the map. 
        
        Returns:
            Keys view of the internal map.
        """
        return self.headers_map.keys()
    
    def values(self):
        """Returns values from the map. 
        
        Returns:
            Values view of the internal map.
        """
        return self.headers_map.values()
    
    def pop(self, name: HeaderName, default: str | None = None) -> str | None:
        """Removes and returns a header value. 
        
        Args:
            name: The header name.
            default: Value to return if not found.
            
        Returns:
            The header value or default.
        """
        name = _ensure_header_name(name)
        if name in self.headers_map:
            value = self.headers_map[name]
            self.remove(name)
            return value
        return default
    
    def popitem(self) -> tuple[HTTPHeader | istr, str]:
        """Removes and returns the last added header. 
        
        Returns:
            A tuple of (name, value).
            
        Raises:
            KeyError: If empty.
        """
        if not self.headers:
            raise KeyError("Headers is empty")
        header = self.headers.pop()
        del self.headers_map[header.name]
        return (header.name, header.value)
    
    def setdefault(self, name: HeaderName, default: str = "") -> str:
        """Returns value if exists, else sets and returns default. 
        
        Args:
            name: The header name.
            default: The default value.
            
        Returns:
            The header value.
        """
        name = _ensure_header_name(name)
        if name in self.headers_map:
            return self.headers_map[name]
        self.add_raw(name, default)
        return default
    
    def replace(self, name: HeaderName, value: str) -> None:
        """Replaces a header value (alias for __setitem__). 
        
        Args:
            name: The header name.
            value: The new value.
        """
        name = _ensure_header_name(name)
        self.remove(name)
        self.add_raw(name, value)
    
    def rename(self, old_name: HeaderName, new_name: HeaderName) -> None:
        """Renames a header, preserving value(s). 
        
        Args:
            old_name: The current header name.
            new_name: The new header name.
        """
        old_name = _ensure_header_name(old_name)
        new_name = _ensure_header_name(new_name)
        if old_name in self.headers_map:
            values = self.get_all(old_name)
            self.remove(old_name)
            for value in values:
                self.add_raw(new_name, value)
    
    def normalize(self) -> None:
        """Normalizes header names in the collection."""
        normalized_headers = []
        for header in self.headers:
            normalized_name = _ensure_header_name(header.name)
            normalized_headers.append(Header(normalized_name, header.value))
        self.headers = normalized_headers
        self.headers_map.clear()
        for header in self.headers:
            self.headers_map.add(header.name, header.value)
    
    def clear_duplicates(self) -> None:
        """Removes duplicate headers, keeping the first occurrence."""
        seen = set()
        unique_headers = []
        for header in self.headers:
            if header.name not in seen:
                seen.add(header.name)
                unique_headers.append(header)
        self.headers = unique_headers
        self.headers_map.clear()
        for header in self.headers:
            self.headers_map[header.name] = header.value
    
    @classmethod
    def build_from_dict(cls, headers_dict: dict[str, str]) -> "Headers":
        """Builds Headers from a dictionary. 
        
        Args:
            headers_dict: Dictionary of {name: value}.
            
        Returns:
            A new Headers instance.
        """
        headers = cls()
        for name, value in headers_dict.items():
            headers.add_raw(name, value)
        return headers
    
    @classmethod
    def build_from_tuples(cls, headers_tuples: list[tuple[str, str]]) -> "Headers":
        """Builds Headers from a list of tuples. 
        
        Args:
            headers_tuples: List of (name, value).
            
        Returns:
            A new Headers instance.
        """
        headers = cls()
        for name, value in headers_tuples:
            headers.add_raw(name, value)
        return headers
    
    @classmethod
    def build_from_list(cls, headers_list: list[Header]) -> "Headers":
        """Builds Headers from a list of Header objects. 
        
        Args:
            headers_list: List of Header objects.
            
        Returns:
            A new Headers instance.
        """
        return cls(headers_list.copy())
