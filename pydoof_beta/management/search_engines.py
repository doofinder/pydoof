from pydoof_beta.api_client import ApiClient

__ALL__ = ('SearchEngines')


class SearchEngines():
    """
    """
    @staticmethod
    def __class_url():
        return '/api/v2/search_engines'

    @staticmethod
    def __instance_url(hashid):
        return f'/api/v2/search_engines/{hashid}'

    @staticmethod
    def __process_url(hashid):
        return f'/api/v2/search_engines/{hashid}/_process'

    @classmethod
    def list(cls, **opts):
        api_client = ApiClient(**opts)
        return api_client.get(
            cls.__class_url()
        )

    @classmethod
    def create(cls, data, **opts):
        api_client = ApiClient(**opts)
        return api_client.post(
            cls.__class_url(),
            data
        )

    @classmethod
    def get(cls, hashid, **opts):
        api_client = ApiClient(**opts)
        return api_client.get(
            cls.__instance_url(hashid)
        )

    @classmethod
    def update(cls, hashid, data, **opts):
        api_client = ApiClient(**opts)
        return api_client.patch(
            cls.__instance_url(hashid),
            data
        )

    @classmethod
    def delete(cls, hashid, **opts):
        api_client = ApiClient(**opts)
        api_client.delete(
            cls.__instance_url(hashid)
        )

    @classmethod
    def schedule_process(cls, hashid, **opts):
        api_client = ApiClient(**opts)
        return api_client.post(
            cls.__process_url(hashid)
        )

    @classmethod
    def get_process_status(cls, hashid, **opts):
        api_client = ApiClient(**opts)
        return api_client.get(
            cls.__process_url(hashid)
        )
