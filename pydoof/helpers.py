"""
Collection of functions to assist PyDoof modules.
"""
from collections import Iterable
from datetime import date
from enum import Enum


def parse_query_params(params):
    """
    Parses a query-parameters dictionary into their proper parameters schema.

    Each key value of the dictionary represents a parameter and its value. The
    function parses each key-value based on the value type.

    * Parses dates into a string following the "YYYYMMDD" format.
    * Parses dictionaries like `parameter: {key: value}` into parameter
      `parameter[key]: value`.
    * Parses lists like `parameter: [val0, val1]` into parameter
      `parameter[]: [val0, val1]`.
    * Excludes parameters where its value is `None`.
    """
    query_params = {}
    for param, value in params.items():
        query_params.update(
            _parse_param(param, value)
        )
    return query_params


def _parse_param(param, value):
    query_params = {}

    if isinstance(value, date):
        query_params[param] = value.strftime("%Y%m%d")
    elif isinstance(value, dict):
        for k, v in value.items():
            query_params.update(
                _parse_param(f'{param}[{k}]', v)
            )
    elif isinstance(value, Enum):
        query_params[param] = value.value
    elif not isinstance(value, str) and isinstance(value, Iterable):
        query_params.update(
            _dicts_appends(_parse_param(f'{param}[]', v) for v in value)
        )
    elif value is not None:
        query_params[param] = value

    return query_params


def _dicts_appends(dicts):
    dict_join = {}
    for dict_ in dicts:
        for key, value in dict_.items():
            if key in dict_join:
                try:
                    dict_join[key].append(value)
                except AttributeError:
                    dict_join[key] = [dict_join[key], value]
            else:
                dict_join[key] = value
    return dict_join
