from pydoof_beta.api_client import ApiClient
from pydoof_beta.management.helpers import build_query_params

__ALL__ = ('Stats')


class Stats:
    class devices:
        DESKTOP = 'desktop'
        MOBILE = 'mobile'

    class formats:
        JSON = 'json'
        CSV = 'csv'

    class sources:
        voice = 'voice'

    class types:
        API = 'api_counters'
        QUERY = 'query_counters'

    @classmethod
    def banners(cls, from_, to, hashids=None, banner_id=None, tz=None,
                format_=None, **opts):
        query_params = build_query_params({
            'from': from_,
            'to': to,
            'hashid': hashids,
            'id': banner_id,
            'tz': tz,
            'format': format_
        })
        api_client = ApiClient(**opts)
        return api_client.get(
            '/api/v2/stats/banners',
            query_params
        )

    @classmethod
    def checkouts(cls, from_, to, hashids=None, device=None, tz=None,
                  interval=None, format_=None, **opts):
        query_params = build_query_params({
            'from': from_,
            'to': to,
            'hashid': hashids,
            'device': device,
            'tz': tz,
            'interval': interval,
            'format': format_
        })
        api_client = ApiClient(**opts)
        return api_client.get(
            '/api/v2/stats/checkouts',
            query_params
        )

    @classmethod
    def clicks(cls, from_, to, hashids=None, device=None, tz=None,
               interval=None, format_=None, **opts):
        query_params = build_query_params({
            'from': from_,
            'to': to,
            'hashid': hashids,
            'device': device,
            'tz': tz,
            'interval': interval,
            'format': format_
        })
        api_client = ApiClient(**opts)
        return api_client.get(
            '/api/v2/stats/clicks',
            query_params
        )

    @classmethod
    def clicks_by_query(cls, query, from_, to, hashids=None, device=None,
                        tz=None, interval=None, format_=None, **opts):
        query_params = build_query_params({
            'from': from_,
            'to': to,
            'hashid': hashids,
            'device': device,
            'tz': tz,
            'interval': interval,
            'format': format_
        })
        api_client = ApiClient(**opts)
        return api_client.get(
            f'/api/v2/stats/clicks/by-query/{query}',
            query_params
        )

    @classmethod
    def clicks_top(cls, from_, to, hashids=None, query=None, device=None,
                   tz=None, interval=None, format_=None, **opts):
        query_params = build_query_params({
            'from': from_,
            'to': to,
            'hashid': hashids,
            'query': query,
            'device': device,
            'tz': tz,
            'interval': interval,
            'format': format_
        })
        api_client = ApiClient(**opts)
        return api_client.get(
            '/api/v2/stats/clicks/top',
            query_params
        )

    @classmethod
    def custom_results(cls, from_, to, hashids=None, custom_result_id=None,
                       tz=None, format_=None, **opts):
        query_params = build_query_params({
            'from': from_,
            'to': to,
            'hashid': hashids,
            'id': custom_result_id,
            'tz': tz,
            'format': format_
        })
        api_client = ApiClient(**opts)
        return api_client.get(
            '/api/v2/stats/custom-results',
            query_params
        )

    @classmethod
    def inits(cls, from_, to, hashids=None, device=None, tz=None,
              interval=None, format_=None, **opts):
        query_params = build_query_params({
            'from': from_,
            'to': to,
            'hashid': hashids,
            'device': device,
            'tz': tz,
            'interval': interval,
            'format': format_
        })
        api_client = ApiClient(**opts)
        return api_client.get(
            '/api/v2/stats/inits',
            query_params
        )

    @classmethod
    def redirects(cls, from_, to, hashids=None, redirect_id=None, tz=None,
                  format_=None, **opts):
        query_params = build_query_params({
            'from': from_,
            'to': to,
            'hashid': hashids,
            'id': redirect_id,
            'tz': tz,
            'format': format_
        })
        api_client = ApiClient(**opts)
        return api_client.get(
            '/api/v2/stats/redirects',
            query_params
        )

    @classmethod
    def click_searches(cls, from_, to, dfid, hashids=None, device=None,
                       tz=None, format_=None, **opts):
        query_params = build_query_params({
            'from': from_,
            'to': to,
            'hashid': hashids,
            'tz': tz,
            'device': device,
            'format': format_
        })
        api_client = ApiClient(**opts)
        return api_client.get(
            f'/api/v2/stats/clicks/{dfid}/searches/top',
            query_params
        )

    @classmethod
    def searches(cls, from_, to, hashids=None, device=None, query_name=None,
                 source=None, total_hits=None, tz=None, interval=None,
                 format_=None, **opts):
        query_params = build_query_params({
            'from': from_,
            'to': to,
            'hashid': hashids,
            'device': device,
            'query_name': query_name,
            'source': source,
            'total_hits': total_hits,
            'tz': tz,
            'interval': interval,
            'format': format_
        })
        api_client = ApiClient(**opts)
        return api_client.get(
            '/api/v2/stats/searches',
            query_params
        )

    @classmethod
    def searches_top(cls, from_, to, hashids=None, device=None,
                     query_name=None, exclude=None, total_hits=None,
                     tz=None, interval=None, format_=None, **opts):
        query_params = build_query_params({
            'from': from_,
            'to': to,
            'hashid': hashids,
            'device': device,
            'query_name': query_name,
            'exclude': exclude,
            'total_hits': total_hits,
            'tz': tz,
            'interval': interval,
            'format': format_
        })
        api_client = ApiClient(**opts)
        return api_client.get(
            '/api/v2/stats/searches/top',
            query_params
        )

    @classmethod
    def usage(cls, from_, to, hashids=None, type_=None, format_=None, **opts):
        query_params = build_query_params({
            'from': from_,
            'to': to,
            'hashid[]': hashids,
            'type': type_,
            'format': format_
        })
        api_client = ApiClient(**opts)
        return api_client.get(
            '/api/v2/stats/usage',
            query_params
        )
