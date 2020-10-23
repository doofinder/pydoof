"""
"""
from pydoof.base import APIConnectionError, PyDoofError

# __ALL__ = (
# )


class SearchAPIError(PyDoofError):
    """"""
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
    """"""
    pass


class BadRequestError(SearchAPIError):
    """"""
    pass


class ForbiddenError(SearchAPIError):
    """defexception message: "forbidden", plug_status: 403"""
    pass


class InvalidTransformationError(SearchAPIError):
    """defexception message: "transformation not valid", plug_status: 409"""
    pass


class QueryLimitReachedError(SearchAPIError):
    """defexception message: "Requests Limit Reached", plug_status: 429"""
    pass
