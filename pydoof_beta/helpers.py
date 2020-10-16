""""""
from collections import Iterable
from datetime import date


def build_query_params(params, keep_order=False):
    query_params = {}
    for param, value in params.items():
        query_params.update(
            parse_param(param, value, keep_order)
        )
    return query_params


def parse_param(param, value, keep_order=False):
    query_params = {}
    if isinstance(value, date):
        query_params[param] = value.strftime("%Y%m%d")

    elif isinstance(value, dict):
        for k, v in value.items():
            query_params.update(
                parse_param(f'{param}[{k}]', v, keep_order)
            )

    elif not isinstance(value, str) and isinstance(value, Iterable):

        if keep_order:
            for i, v in enumerate(value):
                query_params.update(
                    parse_param(f'{param}[{i}]', v, keep_order)
                )
        else:
            for i, v in enumerate(value):
                query_params.update(
                    parse_param(f'{param}[{i}]', v, keep_order)
                )

    elif value is not None:
        query_params[param] = value
    return query_params
