from enum import Enum, unique

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


def query(hashid, query, filter_=None, exclude=None, index_name=None,
          query_name=None, sort=None, page=None, rpp=None, transformer=None,
          no_stats=None, **opts):
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


def suggest(hashid, query, filter_=None, exclude=None, sort=None, page=None,
            rpp=None, transformer=None, no_stats=None, **opts):
    """
    Fetchs suggestions for terms based on the items indexed in a search engine.

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
        sort (lst, optional): Indicates a sorting rule for results. If
            sort is a list of strings, each element will define a field to sort
            by in ascending order. If sort is a list of dictionaries, you can
            set the order. For instance, sort: [{'color': 'desc'}] will sort
            results by color name in descending order. If you do not provided
            one, results will be ordered by score in descending order. Default
            to None.
        page (int, optional): Indicates a page of results. If you provide a
            page, `suggest` will return the results from that page. Default to
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
        'sort': sort,
        'page': page,
        'rpp': rpp,
        'transformer': transformer,
        'nostats': no_stats
    })
    api_client = SearchAPIClient(**opts)
    return api_client.get(
        '/5/suggest',
        query_params=query_params
    )
