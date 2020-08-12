from pydoof_core import SearchEnginesApi

from pydoof_beta.management.helpers import (handle_api_errors,
                                            setup_management_api)

__ALL__ = ('SearchEngines')


class SearchEngines():
    @staticmethod
    @handle_api_errors
    def list(**opts):
        api_instance = setup_management_api(SearchEnginesApi, **opts)
        return api_instance.search_engine_list()

    @staticmethod
    @handle_api_errors
    def create(data, **opts):
        api_instance = setup_management_api(SearchEnginesApi, **opts)
        return api_instance.search_engine_create(data).to_dict()

    @staticmethod
    @handle_api_errors
    def get(hashid, **opts):
        api_instance = setup_management_api(SearchEnginesApi, **opts)
        return api_instance.search_engine_show(hashid).to_dict()

    @staticmethod
    @handle_api_errors
    def update(hashid, data, **opts):
        api_instance = setup_management_api(SearchEnginesApi, **opts)
        return api_instance.search_engine_update(data, hashid).to_dict()

    @staticmethod
    @handle_api_errors
    def delete(hashid, **opts):
        api_instance = setup_management_api(SearchEnginesApi, **opts)
        return api_instance.search_engine_delete(hashid).to_dict()

    @staticmethod
    @handle_api_errors
    def schedule_process(hashid, **opts):
        api_instance = setup_management_api(SearchEnginesApi, **opts)
        return api_instance.process(hashid).to_dict()

    @staticmethod
    @handle_api_errors
    def get_process_status(hashid, **opts):
        api_instance = setup_management_api(SearchEnginesApi, **opts)
        return api_instance.process_status(hashid).to_dict()
