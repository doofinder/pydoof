"""
Collection of functions to assist PyDoof modules.
"""
from datetime import date
from enum import Enum
from typing import Any, Iterable, List


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


def _has_dicts(values: List[Any]):
    # Could be possible to check only the first element.
    # Is used on facets and sort, for example.
    return any(isinstance(value, dict) for value in values)


def _parse_param(param: str, value: Any):
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
        if _has_dicts(value):
            params = (_parse_param(f'{param}[{i}]', v)
                      for i, v in enumerate(value))
        else:
            params = (_parse_param(f'{param}[]', v) for v in value)
        query_params.update(
            _dicts_appends(params)
        )
    elif isinstance(value, bool):
        query_params[param] = str(value).lower()
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
