from pydoof_core import SearchEnginesApi

from pydoof.management.helpers import setup_management_api

__ALL__ = ('SearchEngines')


class SearchEngines():
    @staticmethod
    def list(**opts):
        api_instance = setup_management_api(SearchEnginesApi, **opts)
        return api_instance.search_engine_list()

    @staticmethod
    def create(data, **opts):
        api_instance = setup_management_api(SearchEnginesApi, **opts)
        return api_instance.search_engine_create(data).to_dict()

    @staticmethod
    def get(hashid, **opts):
        api_instance = setup_management_api(SearchEnginesApi, **opts)
        return api_instance.search_engine_show(hashid).to_dict()

    @staticmethod
    def update(hashid, data, **opts):
        api_instance = setup_management_api(SearchEnginesApi, **opts)
        return api_instance.search_engine_update(data, hashid).to_dict()

    @staticmethod
    def delete(hashid, **opts):
        api_instance = setup_management_api(SearchEnginesApi, **opts)
        return api_instance.search_engine_delete(hashid).to_dict()

    @staticmethod
    def schedule_process(hashid, **opts):
        api_instance = setup_management_api(SearchEnginesApi, **opts)
        return api_instance.process(hashid).to_dict()

    @staticmethod
    def get_process_status(hashid, **opts):
        api_instance = setup_management_api(SearchEnginesApi, **opts)
        return api_instance.process_status(hashid).to_dict()
