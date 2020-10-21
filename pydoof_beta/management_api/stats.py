from enum import Enum, unique

from pydoof_beta.management_api.api_client import ManagementAPIClient
from pydoof_beta.helpers import parse_query_params


@unique
class Devices(Enum):
    DESKTOP = 'desktop'
    MOBILE = 'mobile'


@unique
class Formats(Enum):
    JSON = 'json'
    CSV = 'csv'


@unique
class Sources(Enum):
    voice = 'voice'


@unique
class Types(Enum):
    API = 'api_counters'
    QUERY = 'query_counters'


def banners(from_, to, hashids=None, banner_id=None, tz=None,
            format_=None, **opts):
    query_params = parse_query_params({
        'from': from_,
        'to': to,
        'hashid': hashids,
        'id': banner_id,
        'tz': tz,
        'format': format_
    })
    api_client = ManagementAPIClient(**opts)
    return api_client.get(
        '/api/v2/stats/banners',
        query_params
    )


def checkouts(from_, to, hashids=None, device=None, tz=None,
              interval=None, format_=None, **opts):
    query_params = parse_query_params({
        'from': from_,
        'to': to,
        'hashid': hashids,
        'device': device,
        'tz': tz,
        'interval': interval,
        'format': format_
    })
    api_client = ManagementAPIClient(**opts)
    return api_client.get(
        '/api/v2/stats/checkouts',
        query_params
    )


def clicks(from_, to, hashids=None, device=None, tz=None,
           interval=None, format_=None, **opts):
    query_params = parse_query_params({
        'from': from_,
        'to': to,
        'hashid': hashids,
        'device': device,
        'tz': tz,
        'interval': interval,
        'format': format_
    })
    api_client = ManagementAPIClient(**opts)
    return api_client.get(
        '/api/v2/stats/clicks',
        query_params
    )


def clicks_by_query(query, from_, to, hashids=None, device=None,
                    tz=None, interval=None, format_=None, **opts):
    query_params = parse_query_params({
        'from': from_,
        'to': to,
        'hashid': hashids,
        'device': device,
        'tz': tz,
        'interval': interval,
        'format': format_
    })
    api_client = ManagementAPIClient(**opts)
    return api_client.get(
        f'/api/v2/stats/clicks/by-query/{query}',
        query_params
    )


def clicks_top(from_, to, hashids=None, query=None, device=None,
               tz=None, interval=None, format_=None, **opts):
    query_params = parse_query_params({
        'from': from_,
        'to': to,
        'hashid': hashids,
        'query': query,
        'device': device,
        'tz': tz,
        'interval': interval,
        'format': format_
    })
    api_client = ManagementAPIClient(**opts)
    return api_client.get(
        '/api/v2/stats/clicks/top',
        query_params
    )


def custom_results(from_, to, hashids=None, custom_result_id=None,
                   tz=None, format_=None, **opts):
    query_params = parse_query_params({
        'from': from_,
        'to': to,
        'hashid': hashids,
        'id': custom_result_id,
        'tz': tz,
        'format': format_
    })
    api_client = ManagementAPIClient(**opts)
    return api_client.get(
        '/api/v2/stats/custom-results',
        query_params
    )


def facets(from_, to, hashids=None, tz=None, format_=None, **opts):
    query_params = parse_query_params({
        'from': from_,
        'to': to,
        'hashid': hashids,
        'tz': tz,
        'format': format_
    })
    api_client = ManagementAPIClient(**opts)
    return api_client.get(
        '/api/v2/stats/facets',
        query_params
    )


def facets_top(from_, to, hashids=None, tz=None, format_=None,
               **opts):
    query_params = parse_query_params({
        'from': from_,
        'to': to,
        'hashid': hashids,
        'tz': tz,
        'format': format_
    })
    api_client = ManagementAPIClient(**opts)
    return api_client.get(
        '/api/v2/stats/facets/top',
        query_params
    )


def inits(from_, to, hashids=None, device=None, tz=None,
          interval=None, format_=None, **opts):
    query_params = parse_query_params({
        'from': from_,
        'to': to,
        'hashid': hashids,
        'device': device,
        'tz': tz,
        'interval': interval,
        'format': format_
    })
    api_client = ManagementAPIClient(**opts)
    return api_client.get(
        '/api/v2/stats/inits',
        query_params
    )


def inits_locations(from_, to, hashids=None, device=None, tz=None,
                    format_=None, **opts):
    query_params = parse_query_params({
        'from': from_,
        'to': to,
        'hashid': hashids,
        'device': device,
        'tz': tz,
        'format': format_
    })
    api_client = ManagementAPIClient(**opts)
    return api_client.get(
        '/api/v2/stats/inits/locations',
        query_params
    )


def redirects(from_, to, hashids=None, redirect_id=None, tz=None,
              format_=None, **opts):
    query_params = parse_query_params({
        'from': from_,
        'to': to,
        'hashid': hashids,
        'id': redirect_id,
        'tz': tz,
        'format': format_
    })
    api_client = ManagementAPIClient(**opts)
    return api_client.get(
        '/api/v2/stats/redirects',
        query_params
    )


def click_searches(from_, to, dfid, hashids=None, device=None,
                   tz=None, format_=None, **opts):
    query_params = parse_query_params({
        'from': from_,
        'to': to,
        'hashid': hashids,
        'tz': tz,
        'device': device,
        'format': format_
    })
    api_client = ManagementAPIClient(**opts)
    return api_client.get(
        f'/api/v2/stats/clicks/{dfid}/searches/top',
        query_params
    )


def searches(from_, to, hashids=None, device=None, query_name=None,
             source=None, total_hits=None, tz=None, interval=None,
             format_=None, **opts):
    query_params = parse_query_params({
        'from': from_,
        'to': to,
        'hashid': hashids,
        'device': device,
        'query_name': query_name,
        'source': source,
        'total_hits': total_hits,
        'tz': tz,
        'interval': interval,
        'format': format_
    })
    api_client = ManagementAPIClient(**opts)
    return api_client.get(
        '/api/v2/stats/searches',
        query_params
    )


def searches_top(from_, to, hashids=None, device=None,
                 query_name=None, exclude=None, total_hits=None,
                 tz=None, interval=None, format_=None, **opts):
    query_params = parse_query_params({
        'from': from_,
        'to': to,
        'hashid': hashids,
        'device': device,
        'query_name': query_name,
        'exclude': exclude,
        'total_hits': total_hits,
        'tz': tz,
        'interval': interval,
        'format': format_
    })
    api_client = ManagementAPIClient(**opts)
    return api_client.get(
        '/api/v2/stats/searches/top',
        query_params
    )


def usage(from_, to, hashids=None, type_=None, format_=None, **opts):
    query_params = parse_query_params({
        'from': from_,
        'to': to,
        'hashid': hashids,
        'type': type_,
        'format': format_
    })
    api_client = ManagementAPIClient(**opts)
    return api_client.get(
        '/api/v2/stats/usage',
        query_params
    )


def query_log_iter(from_, to, hashids=None, **opts):
    query_params = parse_query_params({
        'from': from_,
        'to': to,
        'hashid': hashids
    })

    api_client = ManagementAPIClient(**opts)
    return api_client.request(
        'GET',
        '/api/v2/stats/query_log',
        query_params,
        stream=True
    )
