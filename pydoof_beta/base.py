"""
Common resources for management and search modules.
"""


class PyDoofError(Exception):
    """Generic PyDoof Error"""
    def __init__(self, code=None, details=None, message=None, error_body=None):
        if error_body:
            self.code = error_body.get('code')
            self.details = error_body.get('details')
            self.message = error_body.get('message')
        else:
            self.code = code
            self.details = details
            self.message = message

    def __str__(self):
        """Custom error messages for exception"""
        error_message = f"({self.code})\n"
        if self.message:
            error_message += f"Message: {self.message}\n"
        if self.details:
            error_message += f"Details: {self.details}\n"

        return error_message
