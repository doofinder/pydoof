from pydoof_beta.base import ApiClient
import pydoof_beta


class SearchApiClient(ApiClient):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        host = kwargs.get('search_host') or pydoof_beta.search_host
        if host is None:
            zone = kwargs.get('zone') or pydoof_beta.zone
            host = f'https://{zone}-search.doofinder.com'

        self.host = host

    def __handle_response_error(self, response):
        return Exception()
