from typing import Optional
from pydoof.helpers import parse_query_params
from pydoof.search_api.api_client import SearchAPIClient


def init_session(hashid: str, session_id: str, **opts):
    """
    Returns number of total unique search sessions in a period group by date.

    Args:
        hashid: Unique search engine id. Indicates to which search engine we are doing the query.
        session_id (<= 32 characters): The current session ID, must be unique for each user.
    """
    query_params = parse_query_params({
        'session_id': session_id,
    })

    api_client = SearchAPIClient(**opts)
    return api_client.put(
        f'/6/{hashid}/stats/init',
        query_params=query_params
    )


def log_checkout(hashid: str, session_id: str, **opts):
    """
    That is the event for when a customer complete a checkout.
    The info of the items that were in her session when she completes the checkout are logged in the event.

    Args:
        hashid: Unique search engine id. Indicates to which search engine we are doing the query.
        session_id (<= 32 characters): The current session ID, must be unique for each user.
    """
    query_params = parse_query_params({
        'session_id': session_id
    })

    api_client = SearchAPIClient(**opts)
    return api_client.put(
        f'/6/{hashid}/stats/checkout',
        query_params=query_params
    )


def log_redirect(hashid: str, redirection_id: str, session_id: str, query: Optional[str] = None, ** opts):
    """
    Logs a "redirection triggered" event in stats logs.

    Args:
        hashid: Unique search engine id. Indicates to which search engine we are doing the query.
        redirection_id: Id of redirection. This id is obtained in the search response that has redirect information.
        session_id (<= 32 characters): The current session ID, must be unique for each user.
        query (<= 200 characters): The search term. It must be escaped.
    """
    query_params = parse_query_params({
        'id': redirection_id,
        'session_id': session_id,
        'query': query
    })

    api_client = SearchAPIClient(**opts)
    return api_client.put(
        f'/6/{hashid}/stats/redirect',
        query_params=query_params
    )
        session_id (<= 32 characters): The current session ID, must be unique for each user.
        query (<= 200 characters): The search term. It must be escaped.
    """
    query_params = {
        'id': id,
        'session_id': session_id
    }

    api_client = SearchAPIClient(**opts)
    return api_client.put(
        f'/6/{hashid}/stats/redirect',
        query_params=query_params
    )


def add_to_cart(hashid, index_name, session_id, item_id, amount, title, price,
                **opts):
    """
    Adds an item to the cart, or creates one if it does not exists.
    """
    query_params = {
        'hashid': hashid,
        'datatype': index_name,
        'session_id': session_id,
        'item_id': item_id,
        'amount': amount,
        'title': title,
        'price': price
    }

    api_client = SearchAPIClient(**opts)
    api_client.get(
        '/5/stats/add-to-cart',
        query_params
    )


def remove_from_cart(hashid, index_name, session_id, item_id, amount, **opts):
    """
    Removes amount from the given item in the cart, and deletes if the result
    is lower than 0.
    """
    query_params = {
        'hashid': hashid,
        'datatype': index_name,
        'session_id': session_id,
        'item_id': item_id,
        'amount': amount
    }

    api_client = SearchAPIClient(**opts)
    api_client.get(
        '/5/stats/remove-from-cart',
        query_params
    )


def clear_cart(hashid, session_id, **opts):
    """
    Deletes the cart with all its content.
    """
    query_params = {
        'hashid': hashid,
        'session_id': session_id
    }

    api_client = SearchAPIClient(**opts)
    api_client.get(
        '/5/stats/clear-cart',
        query_params
    )
