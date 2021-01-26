from enum import Enum, unique

from pydoof.management_api.api_client import ManagementAPIClient
from pydoof.helpers import parse_query_params


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
    VOICE = 'voice'


@unique
class Types(Enum):
    API = 'api_counters'
    QUERY = 'query_counters'


def banners(from_, to, hashids=None, banner_id=None, tz=None, format_=None,
            **opts):
    """
    Returns how many times banners have been displayed and clicked in a period,
    grouped by banner id.
    """
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


def checkouts(from_, to, hashids=None, device=None, tz=None, format_=None,
              **opts):
    """
    Returns number of users checkouts in a period grouped by date.
    """
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
        '/api/v2/stats/checkouts',
        query_params
    )


def clicks(from_, to, hashids=None, device=None, tz=None, format_=None,
           **opts):
    """
    Returns number of times a user clicked an item in a period grouped by date.
    """
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
        '/api/v2/stats/clicks',
        query_params
    )


def clicked_items(from_, to, hashids=None, query=None, device=None, limit=None,
                  tz=None, format_=None, **opts):
    """
    Returns most commonly clicked items in a period.
    """
    query_params = parse_query_params({
        'from': from_,
        'to': to,
        'hashid': hashids,
        'query': query,
        'device': device,
        'limit': limit,
        'tz': tz,
        'format': format_
    })
    api_client = ManagementAPIClient(**opts)
    return api_client.get(
        '/api/v2/stats/clicked_items',
        query_params
    )


def clicked_items_searches(from_, to, dfid, hashids=None, device=None, tz=None,
                           format_=None, **opts):
    """
    Returns the most common searched for a clicked item, and how many times it
    has been clicked from those searches.
    """
    query_params = parse_query_params({
        'from': from_,
        'to': to,
        'dfid': dfid,
        'hashid': hashids,
        'device': device,
        'tz': tz,
        'format': format_
    })
    api_client = ManagementAPIClient(**opts)
    return api_client.get(
        '/api/v2/stats/clicked_items/searches',
        query_params
    )


def custom_results(from_, to, hashids=None, custom_result_id=None, tz=None,
                   format_=None, **opts):
    """
    Returns how many times custom results have been displayed and clicked in a
    period, grouped by custom result id.
    """
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
    """
    Returns how many times facets filters have been used in a period, grouped
    by facet field name.
    """
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


def facets_top(from_, to, hashids=None, tz=None, format_=None, **opts):
    """
    Returns most common facets filters used, how many times they have been
    used, and which filter has been applied in a period.
    """
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


def inits(from_, to, hashids=None, device=None, tz=None, format_=None, **opts):
    """
    Returns number of total unique search sessions in a period group by date.
    """
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
        '/api/v2/stats/inits',
        query_params
    )


def inits_locations(from_, to, hashids=None, device=None, tz=None,
                    format_=None, **opts):
    """
    Returns all unique sessions geolocation(longituted and latitude pairs) for
    a period.
    """
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


def redirects(from_, to, hashids=None, redirect_id=None, tz=None, format_=None,
              **opts):
    """
    Returns how many times users have been redirected by a custom redirections,
    and to which url in a period.
    """
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


def sales(from_, to, hashids=None, tz=None, format_=None, **opts):
    """
    Returns the total price for sales checkouts in a period, where session_id
    identifies every sale.
    """
    query_params = parse_query_params({
        'from': from_,
        'to': to,
        'hashid': hashids,
        'tz': tz,
        'format': format_
    })
    api_client = ManagementAPIClient(**opts)
    return api_client.get(
        '/api/v2/stats/sales',
        query_params
    )


def searches(from_, to, hashids=None, device=None, query_name=None,
             source=None, total_hits=None, tz=None, format_=None, **opts):
    """
    Return number of searches in a period grouped by date.
    """
    query_params = parse_query_params({
        'from': from_,
        'to': to,
        'hashid': hashids,
        'device': device,
        'query_name': query_name,
        'source': source,
        'total_hits': total_hits,
        'tz': tz,
        'format': format_
    })
    api_client = ManagementAPIClient(**opts)
    return api_client.get(
        '/api/v2/stats/searches',
        query_params
    )


def searches_top(from_, to, hashids=None, device=None, query_name=None,
                 exclude=None, total_hits=None, tz=None, format_=None, **opts):
    """
    Returns list of most common searches in a period.
    """
    query_params = parse_query_params({
        'from': from_,
        'to': to,
        'hashid': hashids,
        'device': device,
        'query_name': query_name,
        'exclude': exclude,
        'total_hits': total_hits,
        'tz': tz,
        'format': format_
    })
    api_client = ManagementAPIClient(**opts)
    return api_client.get(
        '/api/v2/stats/searches/top',
        query_params
    )


def usage(from_, to, hashids=None, type_=None, format_=None, **opts):
    """
    Returns usage to search engines during a period.
    It sums the query and API requests made to the service.
    """
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
    """
    Returns an iterator with all the queries done to the search API in a
    period.
    """
    query_params = parse_query_params({
        'from': from_,
        'to': to,
        'hashid': hashids
    })

    api_client = ManagementAPIClient(stream=True, **opts)
    return api_client.request(
        'GET',
        '/api/v2/stats/query_log',
        query_params
    )
