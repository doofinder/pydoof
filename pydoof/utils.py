# coding: utf-8

# python imports
from datetime import datetime, date
from six import string_types


def transform_date_to_string_param(date_param):
    if isinstance(date_param, string_types):
        return date_param

    elif isinstance(date_param, int) or isinstance(date_param, float):
        return "{}".format(date_param)

    elif isinstance(date_param, datetime) or isinstance(date_param, date):
        return date_param.strftime("%Y%m%d")
