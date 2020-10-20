"""
"""
from pydoof_beta.base import PyDoofError


__ALL__ = (
    'APITimeoutError',
    'AccessDeniedError',
    'BadGatewayError',
    'BadParametersError',
    'BadRequestError',
    'ConflictError',
    'IndexInternalError',
    'InvalidBoostValueError',
    'InvalidFieldNamesError',
    'ManagementAPIError',
    'NotAuthenticatedError',
    'NotFoundError',
    'SearchEngineLockedError',
    'TooManyItemsError',
    'TooManyRequestsError',
    'TooManyTemporaryError'
)


class ManagementAPIError(PyDoofError):
    """"""
    def __init__(self, code=None, message=None, details=None, http_body=None,
                 http_status=None, **_kwargs):
        self.code = code
        self.message = message
        self.details = details

        self.http_body = http_body
        self.http_status = http_status

    def __str__(self):
        """Custom error messages for exception"""
        error_message = f"({self.http_status})\n"
        if self.message:
            error_message += f"{self.message}\n\n"
        if self.code:
            error_message += f"Code: {self.code}\n"
        if self.details:
            error_message += f"Details: {self.details}\n"
        if self.http_body:
            error_message += f"Response: {self.http_body}\n"
        return error_message


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
    pass


class NotAuthenticatedError(ManagementAPIError):
    """Requests is not authenticated or has wrong token."""
    pass


class NotFoundError(ManagementAPIError):
    """Resource not found."""
    pass


class APITimeoutError(ManagementAPIError):
    """Operation has surpassed time limit."""
    pass


class TooManyItemsError(ManagementAPIError):
    """Requests contains too many items."""
    pass


class TooManyRequestsError(ManagementAPIError):
    """Too many requests by second."""
    pass


class BadRequestError(ManagementAPIError):
    """Generic error for bad requests"""
    pass


class BadParametersError(BadRequestError):
    """Request contains wrong parameter or values."""
    pass


class IndexInternalError(BadRequestError):
    """Error in the internal index engine."""
    pass


class InvalidBoostValueError(BadRequestError):
    """Invalid value for item boost field."""
    pass


class InvalidFieldNamesError(BadRequestError):
    """Items field names contains invalid characters."""
    pass


class ConflictError(ManagementAPIError):
    """Generic error for conflict state"""
    pass


class SearchEngineLockedError(ConflictError):
    """The request search engine is locked by another  operation."""
    pass


class TooManyTemporaryError(ConflictError):
    """There are too many temporary index."""
    pass
