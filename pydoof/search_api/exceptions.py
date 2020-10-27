"""
Collection of all Exceptions raised by Doofinder Search API.
"""
from pydoof.base import APIConnectionError, PyDoofError


class SearchAPIError(PyDoofError):
    """Generic Search API Error."""
    def __init__(self, message=None, http_body=None, http_status=None,
                 **_kwargs):
        self.message = message

        self.http_body = http_body
        self.http_status = http_status

    def __str__(self):
        """Custom error messages for exception"""
        error_message = [f"({self.http_status})"]
        if self.message:
            error_message += [f"{self.message}"]
        if self.http_body:
            error_message += [f"Response: {self.http_body}"]
        return "\n".join(error_message)


class NotFoundError(SearchAPIError):
    """Resource not found."""


class BadRequestError(SearchAPIError):
    """Request contains wrong parameter or values."""


class ForbiddenError(SearchAPIError):
    """Requests is not authenticated or has wrong token."""


class InvalidTransformationError(SearchAPIError):
    """Request transformer ir wrong."""


class QueryLimitReachedError(SearchAPIError):
    """Account has reached her requests limit."""
