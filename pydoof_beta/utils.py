""""""
import pydoof_beta


def download_query_log(file_path, from_, to, hashids=None, **opts):
    with open(file_path, 'wb') as file:
        log_iter = pydoof_beta.Stats.query_log_iter(from_, to, hashids, **opts)
        file.writelines(log_iter)
