""""""
from collections import Iterable
from datetime import date


def build_query_params(params):
    """"""
    query_params = {}
    for param, value in params.items():
        if isinstance(value, date):
            query_params[param] = value.strftime("%Y%m%d")
        elif isinstance(value, dict):
            query_params.update({f'{param}[{k}]': v for k, v in value.items()})
        elif not isinstance(value, str) and isinstance(value, Iterable):
            query_params[f'{param}[]'] = value
        elif value is not None:
            query_params[param] = value
    return query_params
