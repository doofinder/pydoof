from pydoof_beta.api_client import ApiClient
from pydoof_beta.management.helpers import build_query_params


__ALL__ = ('Internals')


class Internals():
    """
    """
    @staticmethod
    def __user_url(user_id):
        return f'/api/v2/internal/users/{user_id}'

    def __searchengine_url(searchengine_hashid):
        return f'/api/v2/internal/search_engines/{searchengine_hashid}'

    @classmethod
    def users_refresh(cls, user_id, **opts):
        api_client = ApiClient(**opts)
        api_client.post(
            cls.__user_url(user_id) + '/refresh'
        )

    @classmethod
    def searchengine_refresh(cls, searchengine_hashid, **opts):
        api_client = ApiClient(**opts)
        api_client.post(
            cls.__searchengine_url(searchengine_hashid) + '/refresh'
        )

    @classmethod
    def searchengine_mappings(cls, searchengine_hashid, indices=None, **opts):
        api_client = ApiClient(**opts)
        return api_client.get(
            cls.__searchengine_url(searchengine_hashid) + '/mappings',
            query_params=build_query_params({'indices': indices})
        )

    @classmethod
    def searchengine_stats_blocked_ips(cls, searchengine_hashid, **opts):
        api_client = ApiClient(**opts)
        return api_client.get(
            cls.__searchengine_url(searchengine_hashid) + '/stats_blocked_ips',
        )
