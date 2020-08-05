[![Build Status](https://api.travis-ci.org/doofinder/pydoof.svg?branch=master)](https://travis-ci.org/doofinder/pydoof)
pydoof
======

Doofiner Python Client (work in progress)

This library is a python wrapper for `Doofinder Management API 1`
and the `Doofinder Search API 4 and 5`

Installation
------------
  pip install pydoof

Usage
-----
**Management API**

```python
import pydoof
pydoof.API_KEY = 'eu1-s34v2sdfs4werdfsfwclsss'

for se in pydoof.SearchEngine.all():
    print se.name
    accepted, task_id = se.process() # Parse and index the data feed of the Search Engine
    se.process_info()  # Get info of the current/most-recent 'process' task
    se.task_info(task_id) # get info of any task
    se.logs()  # Get the last logs of the Search Engine
```

You can also make changes to a specific Search Engine:
```python
# Select the SearchEngine with the hashid identificator
search_engine = pydoof.SearchEngine('abc32sfasdf3vadsfsafass343')

# Get a list of the data types of the SearchEngine
search_engine.get_types()

# Add a type of data to the SearchEngine
search_engine.add_type('product')

# Delete a type of data (and all its items) from the SearchEngine
search_engine.delete_type('product')

# Get an item of the 'product' type
item = search_engine.get_item('product', item_id)

# Add an item to the 'product' type
added_item_id = search_engine.add_item('product', item)

# Add multiple items to the 'product' type

[added_id1, added_id2, added_id3] = search_engine.add_items('product', [item1, item2, item3])

# Delete an item from the 'product' type
search_engine.delete_item('product', item_id)

# Update or create an item to the 'product' type
# If item_id does not exist, the item is created
search_engine.update_item('product', item_id, item)

# Update or create multiple items
# all items need to have "id" property (item1['id'])
search_engine.update_items('product', [item1, item2, item3])

# Iterate over all items of the 'product' type
for item in search_engine.items('product'):
    print item.id
    print item.description

# Obtain daily aggregated stats data for a SearchEngine during a period of time
from_date = datetime.datetime(2016,11,23)
to_date = datetime.datetime(2016,11,30)
for aggregate in search_engine.stats(from_date, to_date):
    print aggregate.date # day
    print aggregate.searches # num. of searches
    print aggregate.clicks # num. of clicks on searched results
    print aggregate.requests # total num. of requests to doofinder
    print aggregate.api # num of api requests to doofinder
    print aggregate.queries # num of search requests to doofinder
    print aggregate.parser # num of parse requests(items parsed/100) to doofinder

# Obtain sorted terms frequency for a SearchEngine during a period of time
from_date = datetime.datetime(2016,11,23)
to_date = datetime.datetime(2016,11,30)

# Ask doofinder to process search engine's feeds
    sucess, task_id = search_engine.process() # task_id for checking later on task progress

# Get info from last processing task
    task_info = search_engine.process_info() # {'state': 'PROCESSING|FAILURE|SUCCESS', ...}

# Get info from a certain task
    task_info = search_engine.task_info() # {'state': 'PROCESSING|FAILURE|SUCCESS', ...}

# Obtain logs for latest processing tasks
    logs = search_engine.logs()

for clicked_item in search_engine.top_terms('clicked', from_date, to_date):
    print clicked_item.count # number of clicks on the item
    print clicked_item.term # title of the clicked item. i.e. "Aiwa AI012 portable mp3 player"

for search_term in search_engine.top_terms('searches', from_date, to_date):
    print search_term.count # pnumber of searches with that term
    print search_term.term # search term. i.e.: "mp3 player"

for opportunity in search_engine.top_terms('opportunities', from_date, to_date):
    # 'opportunities' are search with no results
    print opportunity.count # pnumber of searches with that term
    print opportunity.term # search term. i.e.: "green custom oak"
```

**Search API**

```python
import pydoof
pydoof.API_KEY = 'eu1-s34v2sdfs4werdfsfwclsss' # mandatory for v5

pydoof.SEARCH_VERSION = 5 # use v5 search server (default is 5)


search_engine = pydoof.SearchEngine('abc32sfasdf3vadsfsafass343')

options = search_engine.get_options() # obtaining options from server. (only v5)

query_response = search_engine.query('test query', 1)
query_response.total  # The total number of results
query_response.max_score  # The maximum score obtained
query_response.query_name  # The query_name used by the search algorithm
query_response.facets # aggregated data information

for item in query_response.get_items():
    print item.id
    print item.body

# Making queries with filters and a specific query_name
search_engine.query('test query', 1,
      {
        'brand': ['nike', 'asics'],
        'price': {'gte': 2.45, 'lt': 100}
      },
      'match_and'  # the query_name
)

# Any keyword argument is passed as req parameter
search_engine.query('test query', rpp=12, lang='pt', transformer='dflayer')

# Use of the sort parameter
query_response = search_engine.query(
    query_term='test query',
    sort= [{'namet':'asc'}, {'update_timestamp': 'desc'}])

# You can use lists as keyword arguments, too.
# The will be translated to repeated req parameters
search_engine.query('test query', type=['product', 'article'])
```

Please note **https is mandatory for versions >= 5**

API Documentation
-----------------
[Doofinder Search v5 documentation](https://www.doofinder.com/support/developer/api/search-api)

[Doofinder Management v1 documentation](https://www.doofinder.com/support/developer/api/management-api)


To Run Tests
------------

You need to have `nose` and `HTTPretty` installed.

To run tests:

````shell
$ nosetests
````
