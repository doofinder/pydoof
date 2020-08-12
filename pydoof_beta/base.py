"""
Common resources for management and search modules.
"""
import json


class PyDoofError(Exception):
    """Generic PyDoof Error"""
    def __init__(self, code=None, details=None, message=None, api_exc=None):
        if api_exc:
            try:
                error = json.loads(api_exc.body).get('error', {})
            except json.JSONDecodeError:
                error = {}
            self.code = error.get('code')
            self.details = error.get('details')
            self.message = error.get('message')
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
