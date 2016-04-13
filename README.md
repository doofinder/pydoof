pydoof
======

Doofiner Python Client (work in progress)

This library is a python wrapper for `Doofinder Management API 1`
and the `Doofinder Search API 4`

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

```

**Search API**

```python
import pydoof
pydoof.API_KEY = 'eu1-s34v2sdfs4werdfsfwclsss'

pydoof.SEARCH_VERSION = 5 # use v5 search server (default is 4)

search_engine = pydoof.SearchEngine('abc32sfasdf3vadsfsafass343')

query_response = search_engine.query('test query', 1)
query_response.total  # The total number of results
query_response.max_score  # The maximum score obtained 
query_response.query_name  # The query_name used by the search algorithm

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

API Documentation
-----------------
[Doofinder Search v4 documentation](http://www.doofinder.com/developer/search-api)

[Doofinder Management v1 documentation](http://www.doofinder.com/developer/management-api)


