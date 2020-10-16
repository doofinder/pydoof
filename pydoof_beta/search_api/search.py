from enum import Enum, unique

from pydoof_beta.api_client import SearchApiClient
from pydoof_beta.helpers import build_query_params


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


def _get_search_url():
    return '/5/search'


def query(hashid, query, filter_=None, exclude=None, type_=None,
          query_name=None, sort=None, page=None, rpp=None, transformer=None,
          nostats=None, **opts):
    query_params = build_query_params({
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
        _get_search_url(),
        query_params=query_params
    )


def suggest():
    pass
