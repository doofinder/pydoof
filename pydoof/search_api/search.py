from enum import Enum, unique
from typing import Any, Dict, List

from pydoof.search_api.api_client import SearchAPIClient
from pydoof.helpers import parse_query_params


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


def query(hashid: str, query: str, filter_: Dict[str, Any]=None, exclude: Dict[str, Any]=None,
          index_name: str=None, query_name: str=None, sort: List[Dict[str, str]]=None,
          page: int=None, rpp: int=None, transformer: str=None, no_stats: bool=None, **opts):
    """
    Queries items indexed in a search engine.

    Args:
        hashid (str): Unique search engine id. Indicates to which search engine
            we are doing the query.
        query (str): The terms we are looking for in the items of the search
            engine.
        filter_ (dict, optional): A dictionary that indicates a filter for
            items. For instance, look for those items of color "blue". Default
            to None.
        exclude (dict, optional): A dictionary that indicates an exclude rule
            for items. For instance, exclude those items that belong to `Foo`
            category. Default to None
        index_name (str, optional): A unique name for a search engine index.
            If provided, it will limit result to that index.
        query_name (str, optional): Indicates a query name to used. It could be
            one of "match_and", "match_or", "fuzzy", or "phonetic_text". If you
            do not provide one, search API will select the best one. Default to
            None.
        sort (lst, optional): Indicates a sorting rule for results. If
            sort is a list of strings, each element will define a field to sort
            by in ascending order. If sort is a list of dictionaries, you can
            set the order. For instance, sort: [{'color': 'desc'}] will sort
            results by color name in descending order. If you do not provided
            one, results will be ordered by score in descending order. Default
            to None.
        page (int, optional): Indicates a page of results. If you provide a
            page, `query` will return the results from that page. Default to
            None.
        rpp (int, optional): Indicates how many results to fetch by page,
            minimum 1, maximum 100. Default to 10.
        transformer (str, optional): Indicates a transformation to apply to
            items in result. It could be one of "basic" or "onlyid". If none is
            set, items will not be transformed. Default to None.
        no_stats (bool, optional): Indicates if the query should be recorded
            in search stats. If it is true, it will not be recorded. Default to
            False.
    """
    query_params = parse_query_params({
        'hashid': hashid,
        'query': query,
        'filter': filter_,
        'exclude': exclude,
        'type': index_name,
        'query_name': query_name,
        'sort': sort,
        'page': page,
        'rpp': rpp,
        'transformer': transformer,
        'nostats': no_stats
    })

    api_client = SearchAPIClient(**opts)
    return api_client.get(
        '/5/search',
        query_params=query_params
    )


def suggest(hashid: str, query: str, indices: List[str]=None, stats: bool=None, session_id: str=None, **opts):
    """
    Fetch suggestions for terms based on the items indexed in a search engine.

    Args:
        hashid (str): Unique search engine id. Indicates to which search engine
            we are doing the query.
        query (str): The terms we are looking for in the items of the search
            engine.
        indices (List[str], optional): With the indices parameter you can specify to search within one specific Index.
            If this parameter is not provided, the search will work with all Indices.
            Note that [ and ] characters should be escaped (%5B and %5D) in all cases.
            Example: indices[]=product&indices[]=page; indices=products
        stats (boolean, optional): Enable/Disable this search in stats reports.
        session_id (str, optional, <= 32 characters): The current session ID, must be unique for each user.
    """
    query_params = parse_query_params({
        'query': query,
        'indices': indices,
        'stats': stats,
        'session_id': session_id
    })
    api_client = SearchAPIClient(**opts)
    return api_client.get(
        f'/6/{hashid}/_suggest',
        query_params=query_params
    )
