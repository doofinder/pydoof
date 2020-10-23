""""""
from collections import Iterable
from datetime import date


def parse_query_params(params):
    query_params = {}
    for param, value in params.items():
        query_params.update(
            parse_param(param, value)
        )
    return query_params


def parse_param(param, value):
    query_params = {}

    if isinstance(value, date):
        query_params[param] = value.strftime("%Y%m%d")
    elif isinstance(value, dict):
        for k, v in value.items():
            query_params.update(
                parse_param(f'{param}[{k}]', v)
            )
    elif not isinstance(value, str) and isinstance(value, Iterable):
        query_params.update(
            join_dicts(parse_param(f'{param}[]', v) for v in value)
        )
    elif value is not None:
        query_params[param] = value

    return query_params


def join_dicts(dicts):
    dict_join = {}
    for dict_ in dicts:
        for key, value in dict_.items():
            if key in dict_join:
                dict_join[key].append(value)
            else:
                dict_join[key] = [value]
    return dict_join