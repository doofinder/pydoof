from pydoof_beta.management.helpers import (list_to_query_params,
                                            handle_api_errors,
                                            setup_management_api)

__ALL__ = ('Internals')


class Internals():

    @staticmethod
    @handle_api_errors
    def users_refresh(user_id, **opts):
        api_client = setup_management_api(**opts)
        return api_client.call_api(
            '/api/v2/internal/users/{user_id}/refresh/',
            'POST',
            path_params={'user_id': user_id},
            response_type='str',
            _return_http_data_only=True
        )

    @staticmethod
    @handle_api_errors
    def searchengine_refresh(searchengine_hashid, **opts):
        api_client = setup_management_api(**opts)
        return api_client.call_api(
            '/api/v2/internal/search_engines/{hashid}/refresh/',
            'POST',
            path_params={'hashid': searchengine_hashid},
            response_type='str',
            _return_http_data_only=True
        )

    @staticmethod
    @handle_api_errors
    def searchengine_mappings(searchengine_hashid, indices=None, **opts):
        query_params = None
        if indices is not None:
            query_params = list_to_query_params('indices', indices)

        api_client = setup_management_api(**opts)
        return api_client.call_api(
            '/api/v2/internal/search_engines/{hashid}/mappings',
            'GET',
            path_params={'hashid': searchengine_hashid},
            query_params=query_params,
            response_type='object',
            _return_http_data_only=True
        )

    @staticmethod
    @handle_api_errors
    def searchengine_stats_blocked_ips(searchengine_hashid, **opts):
        api_client = setup_management_api(**opts)
        return api_client.call_api(
            '/api/v2/internal/search_engines/{hashid}/stats_blocked_ips',
            'GET',
            path_params={'hashid': searchengine_hashid},
            response_type='object',
            _return_http_data_only=True
        )
