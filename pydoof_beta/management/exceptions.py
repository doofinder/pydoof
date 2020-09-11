from pydoof_beta.base import PyDoofError


__ALL__ = ('AccessDeniedError', 'BadParametersError', 'IndexInternalError',
           'InvalidBoostValueError', 'InvalidFieldNamesError',
           'NotAuthenticatedError', 'NotFoundError', 'SearchEngineLockedError',
           'TimeoutError', 'TooManyItemsError', 'TooManyRequestsError',
           'TooManyTemporaryError')


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
