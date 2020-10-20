from enum import Enum, unique

from pydoof_beta.search_api.api_client import SearchApiClient
from pydoof_beta.helpers import parse_query_params


@unique
class QueryNames(Enum):
    MATCH_AND = "match_and"
    MATCH_OR = "match_or"
    FUZZY = "fuzzy"
    PHONETIC = "phonetic_text"


@unique
class Transformers(Enum):
    BASIC = "basic"
    ONLY_IDS = "onlyid"


def query(hashid, query, filter_=None, exclude=None, type_=None,
          query_name=None, sort=None, page=None, rpp=None, transformer=None,
          nostats=None, **opts):
    query_params = parse_query_params({
        'hashid': hashid,
        'query': query,
        'filter': filter_,
        'exclude': exclude,
        'type': type_,
        'query_name': query_name,
        'sort': sort,
        'page': page,
        'rpp': rpp,
        'transformer': transformer,
        'nostats': nostats
    })

    api_client = SearchApiClient(**opts)
    return api_client.get(
        '/5/search',
        query_params=query_params
    )


def suggest(hashid, query, filter_=None, exclude=None, sort=None, page=None,
            rpp=None, transformer=None, nostats=None, **opts):
    query_params = parse_query_params({
        'hashid': hashid,
        'query': query,
        'filter': filter_,
        'exclude': exclude,
        'sort': sort,
        'page': page,
        'rpp': rpp,
        'transformer': transformer,
        'nostats': nostats
    })
    api_client = SearchApiClient(**opts)
    return api_client.get(
        '/5/suggest',
        query_params=query_params
    )
