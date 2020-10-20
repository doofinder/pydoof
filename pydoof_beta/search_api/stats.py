from pydoof_beta.search_api.api_client import SearchApiClient


def add_to_cart(hashid, datatype, session_id, item_id, amount, title, price,
                **opts):
    query_params = {
        'hashid': hashid,
        'datatype': datatype,
        'session_id': session_id,
        'item': item_id,
        'amount': amount,
        'title': title,
        'price': price
    }

    api_client = SearchApiClient(**opts)
    api_client.get(
        '/5/stats/add-to-cart',
        query_params
    )


def remove_from_cart(hashid, datatype, session_id, item_id, amount, title,
                     price, **opts):
    query_params = {
        'hashid': hashid,
        'datatype': datatype,
        'session_id': session_id,
        'item': item_id,
        'amount': amount,
        'title': title,
        'price': price
    }

    api_client = SearchApiClient(**opts)
    api_client.get(
        '/5/stats/remove-from-cart',
        query_params
    )


def clear_cart(hashid, session_id, **opts):
    query_params = {
        'hashid': hashid,
        'session_id': session_id
    }

    api_client = SearchApiClient(**opts)
    api_client.get(
        '/5/stats/clear-cart',
        query_params
    )


def checkout(hashid, session_id, **opts):
    query_params = {
        'hashid': hashid,
        'session_id': session_id
    }

    api_client = SearchApiClient(**opts)
    api_client.get(
        '/5/stats/checkout',
        query_params
    )
