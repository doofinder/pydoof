"""
Collection of all Exceptions raised by Doofinder Management API.
"""
from pydoof.base import APIConnectionError, PyDoofError


class ManagementAPIError(PyDoofError):
    """Generic Management API Error."""
    def __init__(self, code=None, message=None, details=None, http_body=None,
                 http_status=None, **_kwargs):
        self.code = code
        self.message = message
        self.details = details

        self.http_body = http_body
        self.http_status = http_status

    def __str__(self):
        """Custom error messages for exception"""
        error_message = [f"({self.http_status})"]
        if self.message:
            error_message += [f"{self.message}"]
        if self.code:
            error_message += [f"Code: {self.code}"]
        if self.details:
            error_message += [f"Details: {self.details}"]
        if self.http_body:
            error_message += [f"Response: {self.http_body}"]
        return "\n".join(error_message)


class BadGatewayError(ManagementAPIError):
    """Bad Gateway Error connecting to Doofinder."""
    def __init__(self, **kwargs):
        super(BadGatewayError, self).__init__(**kwargs)
        if self.message is None:
            self.message = ("Unexpected error communicating with Doofinder. "
                            "If this problem persists, let us know at "
                            "support@doofinder.com.")


class AccessDeniedError(ManagementAPIError):
    """User has no permission to access resource."""


class NotAuthenticatedError(ManagementAPIError):
    """Requests is not authenticated or has wrong token."""


class NotFoundError(ManagementAPIError):
    """Resource not found."""


class APITimeoutError(ManagementAPIError):
    """Operation has surpassed time limit."""


class TooManyItemsError(ManagementAPIError):
    """Requests contains too many items."""


class TooManyRequestsError(ManagementAPIError):
    """Too many requests by second."""


class BadRequestError(ManagementAPIError):
    """Generic error for bad requests"""


class BadParametersError(BadRequestError):
    """Request contains wrong parameter or values."""


class IndexInternalError(BadRequestError):
    """Error in the internal index engine."""


class InvalidBoostValueError(BadRequestError):
    """Invalid value for item boost field."""


class InvalidFieldNamesError(BadRequestError):
    """Items field names contains invalid characters."""


class ConflictError(ManagementAPIError):
    """Generic error for conflict state"""


class SearchEngineLockedError(ConflictError):
    """The request search engine is locked by another  operation."""


class TooManyTemporaryError(ConflictError):
    """There are too many temporary index."""
