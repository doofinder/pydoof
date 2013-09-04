class NotAllowed(Exception):
    """ raised when auth fails"""
    pass

class WrongResponse(Exception):
    """ raised when response can't be parsed"""
    pass

class BadRequest(Exception):
    """ raised when the client makes a bad request"""
    pass
