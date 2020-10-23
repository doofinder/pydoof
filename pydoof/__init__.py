token = None
_dfmaster_token = None

management_url = None
search_url = None


from pydoof.management_api import indices, items, search_engines
from pydoof.management_api import stats as management_stats

from pydoof.search_api import search
from pydoof.search_api import stats as search_stats
