from functools import wraps

from pydoof_core import ApiClient, Configuration
from pydoof_core.rest import ApiException

from pydoof_beta.management.exceptions import _get_exception_class
import pydoof_beta


def handle_api_errors(func):
    """
    """
    return func
    # Disable while refactoring
    # @wraps(func)
    # def handle_errors(*args, **kwargs):
    #     try:
    #         return func(*args, **kwargs)
    #     except ApiException as exc:
    #         pydoof_exc_class = _get_exception_class(exc)
    #         raise pydoof_exc_class(api_exc=exc) from exc
    # return handle_errors


def bulk_request(hashid, name, items, temp, method, **opts):
    """
    """
    query_params = []
    if 'raw' in opts:
        query_params += [('raw', 1)]
    if 'destination_server' in opts:
        query_params += [('destination_server', opts['destination_server'])]

    url = '/api/v2/search_engines/{hashid}/indices/{name}/items/_bulk'
    if temp:
        url = '/api/v2/search_engines/{hashid}/indices/{name}/temp/items/_bulk'

    api_client = setup_management_api(**opts)
    return api_client.call_api(
        url,
        method,
        path_params={'hashid': hashid, 'name': name},
        query_params=query_params,
        body=items,
        auth_settings=['api_token'],
        response_type='object',
        _return_http_data_only=True
    )


def get_management_host(**opts):
    """
    """
    zone = opts.get('zone') or pydoof_beta.zone
    host = opts.get('management_host') or pydoof_beta.management_host

    if host is None:
        return f'https://{zone}-api.doofinder.com'
    return host


def list_to_query_params(param_name, param_values):
    """
    """
    return [(f'{param_name}[]', param) for param in param_values]


def setup_management_api(klass=None, **opts):
    """
    """
    dfmaster_token = opts.get('_dfmaster_token') or pydoof_beta._dfmaster_token
    token = opts.get('token') or pydoof_beta.token
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
