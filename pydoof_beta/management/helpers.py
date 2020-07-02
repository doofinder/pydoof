from pydoof_core import ApiClient, Configuration

import pydoof_beta


def get_management_host(**opts):
    """
    """
    zone = opts.get('zone') or pydoof.zone
    host = opts.get('management_host') or pydoof.management_host

    if host is None:
        return f'https://{zone}-api.doofinder.com'
    return host


def setup_management_api(klass=None, **opts):
    """
    """
    dfmaster_token = opts.get('dfmaster_token') or pydoof._dfmaster_token
    token = opts.get('token') or pydoof.token
    host = get_management_host(**opts)

    configuration = Configuration()
    configuration.api_key['Authorization'] = f'Token {token}'
    configuration.host = host

    api_client = ApiClient(configuration)
    if dfmaster_token is not None:
        api_client.set_default_header('dfmastertoken', dfmaster_token)

    if klass is None:
        return api_client
    return klass(api_client)


def list_to_query_params(param_name, param_values):
    """
    """
    return [(f'{param_name}[]', param) for param in param_values]
