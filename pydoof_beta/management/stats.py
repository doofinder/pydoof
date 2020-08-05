from pydoof_beta.management.helpers import (list_to_query_params,
                                            setup_management_api)

__ALL__ = ('Stats')

__COMMON_PARAMS__ = {
    'response_type': object,
    'auth_settings': ['api_token'],
    '_return_http_data_only': True
}


class Stats:
    class devices:
        DESKTOP = 'desktop'
        MOBILE = 'mobile'

    class formats:
        JSON = 'json'
        CSV = 'csv'

    class types:
        API = 'api_counters'
        QUERY = 'query_counters'

    @staticmethod
    def searches_by_click(from_, to, dfid, hashids=None, tz=None,
                          device=None, format_=None, **opts):
        query_params = [('from', from_), ('to', to)]
        if hashids is not None:
            query_params += list_to_query_params('hashid', hashids)
        if tz is not None:
            query_params += [('tz', tz)]
        if device is not None:
            query_params += [('device', device)]
        if format_ is not None:
            query_params += [('format', format_)]

        api_client = setup_management_api(**opts)
        return api_client.call_api(
            '/api/v2/stats/searches/top', 'GET',
            query_params=query_params,
            **__COMMON_PARAMS__
        )

    @staticmethod
    def searches_top(from_, to, hashids=None, tz=None, device=None,
                     format_=None, query_name=None, total_hits=None,
                     exclude=None, **opts):
        query_params = [('from', from_), ('to', to)]
        if hashids is not None:
            query_params += list_to_query_params('hashid', hashids)
        if tz is not None:
            query_params += [('tz', tz)]
        if device is not None:
            query_params += [('device', device)]
        if format_ is not None:
            query_params += [('format', format_)]
        if query_name is not None:
            query_params += [('query_name', query_name)]
        if total_hits is not None:
            query_params += [('total_hits', total_hits)]
        if exclude is not None:
            query_params += [('exclude', exclude)]

        api_client = setup_management_api(**opts)
        return api_client.call_api(
            '/api/v2/stats/searches/top', 'GET',
            query_params=query_params,
            **__COMMON_PARAMS__
        )

    @staticmethod
    def usage(from_, to, hashids=None, type_=None, format_=None, **opts):
        query_params = [('from', from_), ('to', to)]
        if hashids is not None:
            query_params += list_to_query_params('hashid', hashids)
        if type_ is not None:
            query_params += [('type', type_)]
        if format_ is not None:
            query_params += [('format', format_)]

        api_client = setup_management_api(**opts)
        return api_client.call_api(
            '/api/v2/stats/usage', 'GET',
            query_params=query_params,
            **__COMMON_PARAMS__
        )
