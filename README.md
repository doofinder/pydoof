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
pydoof.API_KEY = 's34v2sdfs4werdfsfwclsss-eu1'

for se in pydoof.SearchEngine.all():
    print se.name
    accepted, task_id = se.process()  # Parse and index the data feed of the Search Engine
    se.info(task_id)  # Get info of the task
    se.logs()  # Get the last logs of the Search Engine tasks
```

You can also make changes to a specific Search Engine:
```python
# Select the SearchEngine with the hashid identificator
search_engine = pydoof.SearchEngine('abc32sfasdf3vadsfsafass343')

# Get a list of the datatypes of the SearchEngine
search_engine.get_datatypes()

# Get an item of the 'product' datatype
item = search_engine.get_item('product', item_id)

# Add an item
search_engine.add_item('product', item)

# Delete an item
search_engine.delete_item('product', item_id)

# Update an item
search_engine.update_item('product', item_id, item)

# Iterate over all items
for item in search_engine.items('product'):
    print item.id
    print item.description

# Get the 2nd page of items (from numbers 11 to 20)
search_engine.items('product', 2)
```

**Search API**

```python
import pydoof
pydoof.SEARCH_DOMAIN = 'eu1-search.doofinder.com'

search_engine = pydoof.SearchEngine('abc32sfasdf3vadsfsafass343')

query_response = search_engine.query('test query', 1)
query_response.total  # The total number of results
query_response.max_score  # The maximum score obtained 
query_response.query_name  # The query_name used by the search algorithm

for item in query_response.get_items():
    print item.id
    print item.description

# Making queries with filters and a specific query_name
search_engine.query('test query', 1, 
      {
        'brand': ['nike', 'asics'],
        'price': {'from': 2.45, 'to': 100}
      },
      'match_and'  # the query_name
)
```

API Documentation
-----------------
[Doofinder Search v4 documentation](http://www.doofinder.com)

[Doofinder Management v1 documentation](http://www.doofinder.com)


