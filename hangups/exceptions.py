"""Exceptions used by hangups."""

class HangupsError(Exception):
    """hangups general exception."""
    pass


class NetworkError(HangupsError):
    """hangups network operation failed."""
    pass

class ParseError(HangupsError):
    """hangups failed to parse a message."""
    pass
