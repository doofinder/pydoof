from enum import Enum, unique
from typing import Any, Dict, List

from pydoof.search_api.api_client import SearchAPIClient
from pydoof.helpers import parse_query_params


@unique
class QueryNames(Enum):
    MATCH_AND = "match_and"
    MATCH_OR = "match_or"
    FUZZY = "fuzzy"


@unique
class SearchFilterExecution(Enum):
    AND = "and"
    OR = "or"


def query(hashid: str, query: str = '', auto_filters: bool = None, custom_results: bool = None,
          excluded_results: bool = None, filter: Dict[str, Any] = None,
          exclude: Dict[str, Any] = None,
          indices: List[str] = None, query_name: QueryNames = None,
          sort: List[Dict[str, str]] = None, page: int = None, rpp: int = None,
          facets: List[Dict[str, Any]] = None, filter_execution: SearchFilterExecution = None,
          session_id: str = None, stats: bool = None, skip_auto_filters: List[str] = None,
          skip_top_facet: List[str] = None, title_facet: bool = None, top_facet: bool = None, **opts):
    """
    Queries items indexed in a search engine.

    Args:
        hashid (str): Unique search engine id. Indicates to which search engine
            we are doing the query.
        query (str): The terms we are looking for in the items of the search engine. Default to ''
        auto_filters (boolean, optional): Enable/Disable the automatic filters in search.
            Default: None.
        custom_results (boolean, optional): Enable/Disable the custom results in search.
            Default: None.
        excluded_results (boolean, optional): Enable/Disable the excluded results in search.
            Default: None.
        filter (dict, optional): A dictionary that indicates a filter for
            items. For instance, look for those items of color "blue".
            Default to None.
        exclude (dict, optional): A dictionary that indicates an exclude rule
            for items. For instance, exclude those items that belong to `Foo`
            category. Default to None
        indices (list, optional): With the indices parameter you can specify to search within one specific Index.
            Default: None
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
            minimum 1, maximum 100. Default to None.
        facets (list, optional): Indicates a list with dicts of facets to fetch.
            An object with field is required, size is optional (max 100).
        filter_execution (SearchQueryName, optional): If you want you can change it to "or".
            Default to None.
        stats (bool, optional): Enable/Disable this search in stats reports.
            Default: None
        skip_auto_filters (list, optional): A list of fields to be skipped from auto_filters feature.
        skip_top_facet (list, optional): A list of fields to be skipped from top_facet feature.
        title_facet (bool, optional): Enable/Disable title_facet feature.
            Default: None.
        top_facet (bool, optional): Enable/Disable top_facet feature.
            Default: None.
    """
    query_params = parse_query_params({
        'hashid': hashid,
        'query': query,
        'auto_filters': auto_filters,
        'custom_results': custom_results,
        'excluded_results': excluded_results,
        'filter': filter,
        'exclude': exclude,
        'query_name': query_name,
        'indices': indices,
        'sort': sort,
        'page': page,
        'rpp': rpp,
        'facets': facets,
        'filter_execution': filter_execution,
        'session_id': session_id,
        'stats': stats,
        'skip_auto_filters': skip_auto_filters,
        'skip_top_facet': skip_top_facet,
        'title_facet': title_facet,
        'top_facet': top_facet
    })

    api_client = SearchAPIClient(**opts)
    return api_client.get(
        f'/6/{hashid}/_search',
        query_params=query_params
    )


def suggest(hashid: str, query: str = '', indices: List[str] = None, stats: bool = None, session_id: str = None, **opts):
    """
    Fetch suggestions for terms based on the items indexed in a search engine.

    Args:
        hashid (str): Unique search engine id. Indicates to which search engine
            we are doing the query.
        query (str): The terms we are looking for in the items of the search engine. Default to ''.
        indices (List[str], optional): With the indices parameter you can specify to search within one specific Index.
            If this parameter is not provided, the search will work with all Indices.
            Note that [ and ] characters should be escaped (%5B and %5D) in all cases.
            Example: indices[]=product&indices[]=page; indices=products
        stats (boolean, optional): Enable/Disable this search in stats reports.
            Default: None.
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
