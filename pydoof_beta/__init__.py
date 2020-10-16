token = None
zone = None
_dfmaster_token = None

management_host = None
search_host = None


from pydoof_beta.management_api import indices, items, search_engines
from pydoof_beta.management_api import stats as management_stats
from pydoof_beta.management_api.items import Scroll
from pydoof_beta.management_api.stats import Devices, Formats, Sources, Types

from pydoof_beta.search_api.search import QueryNames, Transformers
from pydoof_beta.search_api import search, stats
from pydoof_beta.search_api import stats as search_stats
