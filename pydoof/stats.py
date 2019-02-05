# coding: utf-8

"""
    Doofinder API v2 Stats wrapper

    This wrapper is the exposed part of the library to allow
    using the code correctly and handle some hairy details by
    ourselves and free the integrator of dealing with them.
"""

# python imports
import inspect
from six import with_metaclass

# Swagger imports
from swagger_client.api.stats_api import StatsApi
from swagger_client.api_client import ApiClient

# Project imports
from pydoof.configuration import get_configuration, EU_REGION
from pydoof.utils import transform_date_to_string_param


def api_call_decorator(func):
    """
    Decorator to make the authorization and common parameters
    work as intended
    """
    def wrapper(self, hashid, **kwargs):
        # Manage the authorization
        config = self.api_client.configuration
        if config.jwt_token:
            authorization = "Bearer {}".format(config.get_token())

        else:
            authorization = "Bearer {}".format(config.key)

        # Transform hashids if it's a list
        if type(hashid) == list:
            hashid = "[" + ",".join(hashid) + "]"

        # Transform dfrom and dto from datetime's formats to string dates
        if "dfrom" in kwargs:
            dfrom_str = transform_date_to_string_param(kwargs["dfrom"])
            kwargs.update({"dfrom": dfrom_str})

        if "dto" in kwargs:
            dto_str = transform_date_to_string_param(kwargs["dto"])
            kwargs.update({"dto": dto_str})

        if "tz" not in kwargs:
            tz = "+00:00"
            kwargs.update({"tz": tz})

        print(kwargs)

        return func(self, authorization, hashid, **kwargs)

    return wrapper


class StatsMeta(type):
    """
    Metaclass to help create and adjust a more easy class to
    fetch stats from Doofinder API v2, using what Swagger
    generates as the template.
    """

    def __new__(cls, name, bases, dct):
        # Fetch methods from StatsApi from Swagger
        members = inspect.getmembers(StatsApi, predicate=inspect.isfunction)

        for func_name, func in members:
            # Add decoration
            if (not func_name.startswith("__") and
                    "with_http_info" not in func_name):
                dct[func_name] = api_call_decorator(func)

            elif func_name != "__init__":
                # Do not overwrite our custom __init__ method
                dct[func_name] = func

        # Ready to create it
        x = type.__new__(cls, name, bases, dct)
        return x


class DoofinderStats(with_metaclass(StatsMeta)):
    def __init__(self, key=None, region=EU_REGION, configuration=None):
        if configuration:
            api_client = ApiClient(configuration=configuration)

        elif key:
            config = get_configuration(key, region)
            api_client = ApiClient(configuration=config)

        else:
            raise TypeError("Missing key for authentication")

        StatsApi.__init__(self, api_client=api_client)
