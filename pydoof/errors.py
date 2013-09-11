import requests

class NotAllowed(Exception):
    """ raised when auth fails"""
    pass

class WrongResponse(Exception):
    """ raised when response can't be parsed"""
    pass

class BadRequest(Exception):
    """ raised when the client makes a bad request"""
    pass

def handle_errors(r):
    if r.status_code == requests.codes.forbidden:
        raise NotAllowed("The user does not have permissions to "
                        "perform this operation: %s" % r.text)
    if r.status_code == requests.codes.unauthorized:
        raise NotAllowed("The user hasn't provided valid authorization: %s" %
                         r.text)
    if r.status_code == requests.codes.not_found:
        raise BadRequest("Not Found: %s" % r.text)
    if r.status_code == requests.codes.conflict: # when trying to post with a
        raise BadRequest("Request conflict: %s" % r.text) # used doc_id
    if r.status_code > 500:
        raise WrongResponse("Server error: %s" % r.text)
    if r.status_code > 400:
        raise BadRequest("The client made a bad request: %s" % r.text)

