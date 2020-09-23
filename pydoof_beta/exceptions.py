"""
"""
__ALL__ = ('AccessDeniedError', 'BadParametersError', 'IndexInternalError',
           'InvalidBoostValueError', 'InvalidFieldNamesError',
           'NotAuthenticatedError', 'NotFoundError', 'SearchEngineLockedError',
           'TimeoutError', 'TooManyItemsError', 'TooManyRequestsError',
           'TooManyTemporaryError')


class PyDoofError(Exception):
    """Generic PyDoof Error"""
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


class APIConnectionError(PyDoofError):
    def __init__(self, message=None, original_exc=None):
        self.message = message
        self.original_exc = original_exc

    def __str__(self):
        error_message = "\n"
        if self.message:
            error_message += f"{self.message}\n\n"
        if self.original_exc:
            error_message += f"{type(self.original_exc).__name__}"
            if str(self.original_exc):
                error_message += f": {str(self.original_exc)}"
        return error_message


class BadGatewayError(PyDoofError):
    """Bad Gateway Error connecting to Doofinder."""
    pass


class AccessDeniedError(PyDoofError):
    """User has no permission to access resource."""
    pass


class NotAuthenticatedError(PyDoofError):
    """Requests is not authenticated or has wrong token."""
    pass


class NotFoundError(PyDoofError):
    """Resource not found."""
    pass


class APITimeoutError(PyDoofError):
    """Operation has surpassed time limit."""
    pass


class TooManyItemsError(PyDoofError):
    """Requests contains too many items."""
    pass


class TooManyRequestsError(PyDoofError):
    """Too many requests by second."""
    pass


class BadRequestError(PyDoofError):
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


class ConflictError(PyDoofError):
    """Generic error for conflict state"""
    pass


class SearchEngineLockedError(ConflictError):
    """The request search engine is locked by another  operation."""
    pass


class TooManyTemporaryError(ConflictError):
    """There are too many temporary index."""
    pass
