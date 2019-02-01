# coding: utf-8

"""
    Doofinder API v2 client wrapper

    This wrapper is the exposed part of the library to allow
    using the code correctly and handle some hairy details by
    ourselves and free the integrator of dealing with them.
"""

# python imports
import time

# Swagger imports
from swagger_client.configuration import Configuration

# 3rd party imports
from jose import jwt

# Constants

EU_REGION = "eu1"
US_REGION = "us1"


def get_configuration(key, region=EU_REGION):
    """
    Subclassing a Configuration object is a complete disaster
    thanks to some meta programming magic, so we go the same
    way to create a tailored config for our API
    """
    # Inject our methods
    Configuration.get_jwt_auth_token = get_jwt_auth_token
    Configuration.create_token = create_token
    Configuration.refresh = refresh
    Configuration.get_token = get_token
    Configuration.is_expired = is_expired
    Configuration._get_timestamp = _get_timestamp

    config = Configuration()

    # Inject our config
    config.key = key
    config.jwt_token = None
    config.token_data = {}
    config.host = "https://{}-api.doofinder.com".format(region)

    return config


def get_jwt_auth_token(self, data={}, expiry=3600):
    """
    Generates a jwt token
    """
    self.token_data = data
    self.create_token(self.key, data, expiry)


def create_token(self, key=None, data={}, expiry=3600):
    """
    Given a key, generates a JWT token signed with it,
    using HMAC256, and some expiry date based ond the
    options given.

    Params:
        key: Key used to generate the token
        expiry: Expiration time in seconds, by default 3600 (1 hour)
        data: Extra dict data added to the JWT token
    """
    now = self._get_timestamp()
    expiry_timestamp = now + expiry
    if key:
        self.key = key

    if data:
        data['iat'] = now
        data['exp'] = expiry_timestamp
        self.token_data.update(data)

    else:
        self.token_data.update({'iat': now,
                            'exp': expiry_timestamp})

    self.expiry = expiry_timestamp
    self.jwt_token = jwt.encode(self.token_data, self.key, algorithm='HS256')


def refresh(self, expiry=3600):
    self.create_token(expiry=expiry)


def get_token(self):
    """
    Returns the current token or regenerates it
    if it has expired
    """
    if self.is_expired():
        self.refresh()

    return self.jwt_token


def is_expired(self):
    """
    Tells if the token has expired
    """
    now = self._get_timestamp()

    return self.expiry < now


def _get_timestamp(self):
    return int(time.time())
