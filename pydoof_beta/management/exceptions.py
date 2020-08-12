import json

from pydoof_beta.base import PyDoofError


__ALL__ = ('AccessDeniedError', 'BadParametersError', 'IndexInternalError',
           'InvalidBoostValueError', 'InvalidFieldNamesError',
           'NotAuthenticatedError', 'NotFoundError', 'SearchEngineLockedError',
           'TimeoutError', 'TooManyItemsError', 'TooManyRequestsError',
           'TooManyTemporaryError')


class AccessDeniedError(PyDoofError):
    """User has no permission to access resource."""
    pass


class BadParametersError(PyDoofError):
    """Request contains wrong parameter or values."""
    pass


class IndexInternalError(PyDoofError):
    """Error in the internal index engine."""
    pass


class InvalidBoostValueError(PyDoofError):
    """Invalid value for item boost field."""
    pass


class InvalidFieldNamesError(PyDoofError):
    """Items field names contains invalid characters."""
    pass


class NotAuthenticatedError(PyDoofError):
    """Requests is not authenticated or has wrong token."""
    pass


class NotFoundError(PyDoofError):
    """Resource not found."""
    pass


class SearchEngineLockedError(PyDoofError):
    """The request search engine is locked by another  operation."""
    pass


class TimeoutError(PyDoofError):
    """Operation has surpassed time limit."""
    pass


class TooManyItemsError(PyDoofError):
    """Requests contains too many items."""
    pass


class TooManyRequestsError(PyDoofError):
    """Too many requests by second."""
    pass


class TooManyTemporaryError(PyDoofError):
    """There are too many temporary index."""
    pass


def _get_exception_class(exc):
    """
    """
    api_errors_map = {
        'access_denied': AccessDeniedError,
        'bad_params': BadParametersError,
        'index_internal_error': IndexInternalError,
        'invalid_boost_value': InvalidBoostValueError,
        'invalid_field_name': InvalidFieldNamesError,
        'not_authenticated': NotAuthenticatedError,
        'not_found': NotFoundError,
        'searchengine_locked': SearchEngineLockedError,
        'timeout': TimeoutError,
        'too_many_items': TooManyItemsError,
        'too_many_requests': TooManyRequestsError,
        'too_many_temporary': TooManyTemporaryError
    }

    try:
        error_code = json.loads(exc.body).get('error', {}).get('code', None)
        klass = api_errors_map.get(error_code, PyDoofError)
    except json.JSONDecodeError:
        klass = PyDoofError
    return klass
