from pydoof_core import IndicesApi

from pydoof_beta.management.helpers import setup_management_api

__ALL__ = ('Indices')


class Indices():
    @staticmethod
    def list(hashid, **opts):
        api_instance = setup_management_api(IndicesApi, **opts)
        return api_instance.index_index(hashid)

    @staticmethod
    def create(hashid, data, **opts):
        api_instance = setup_management_api(IndicesApi, **opts)
        return api_instance.index_create(data, hashid).to_dict()

    @staticmethod
    def create_temp(hashid, name, **opts):
        api_instance = setup_management_api(IndicesApi, **opts)
        api_instance.temporary_index_create(hashid, name)

    @staticmethod
    def get(hashid, name, **opts):
        api_instance = setup_management_api(IndicesApi, **opts)
        return api_instance.index_show(hashid, name).to_dict()

    @staticmethod
    def update(hashid, name, data, **opts):
        api_instance = setup_management_api(IndicesApi, **opts)
        return api_instance.index_update(data, hashid, name).to_dict()

    @staticmethod
    def delete(hashid, name, **opts):
        api_instance = setup_management_api(IndicesApi, **opts)
        api_instance.index_delete(hashid, name)

    @staticmethod
    def delete_temp(hashid, name, **opts):
        api_instance = setup_management_api(IndicesApi, **opts)
        api_instance.temporary_index_delete(hashid, name)

    @staticmethod
    def reindex_to_temp(hashid, name, **opts):
        api_instance = setup_management_api(IndicesApi, **opts)
        api_instance.reindex_to_temp(hashid, name)

    @staticmethod
    def reindex_status(hashid, name, **opts):
        api_instance = setup_management_api(IndicesApi, **opts)
        return api_instance.get_reindexing_status(hashid, name)

    @staticmethod
    def replace_by_temp(hashid, name, **opts):
        api_instance = setup_management_api(IndicesApi, **opts)
        api_instance.replace_by_temp(hashid, name)
