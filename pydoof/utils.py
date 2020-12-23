"""
Collection of utility functions for Doofinder API.
"""
from pydoof.management_api.stats import query_log_iter


def download_query_log(file_path, from_, to, hashids=None, **opts):
    """
    Downloads and saves query search engine/s logs into file.
    """
    with open(file_path, 'wb') as file:
        log_iter = query_log_iter(from_, to, hashids, **opts)
        file.writelines(log_iter)
