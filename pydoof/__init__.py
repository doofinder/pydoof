token = None
_dfmaster_token = None

management_url = None
search_url = None


def _get_suggestions_index(name):
    """Returns suggestions index name for a regular index name."""
    return f'df_suggestions_{name}'


from pydoof.management_api import indices, items, search_engines
from pydoof.management_api import stats as management_stats

from pydoof.search_api import search
from pydoof.search_api import stats as search_stats
