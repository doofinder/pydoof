PyDoof
======
[![Build Status](https://api.travis-ci.org/doofinder/pydoof.svg?branch=master)](https://travis-ci.org/doofinder/pydoof)

PyDoof is a Python client for Doofinder APIs (management and search). It provides easy access to Doofinder endpoint, including parameters-parsing and requests authentication.

Installation
------------
PyDoof can be installed from PyPI:
```
pip install pydoof
```
Or directly from source code:
```
python setup.py install
```

Usage
-----
To configure PyDoof, you need one of your user API keys, and your management and search URLs. You can find that information in the [API Keys section](https://app.doofinder.com/es/admin/api/) of your Doofinder admin page. Set `pydoof.token`, `pydoof.management_url`, and `pydoof.search_url` with those values:

```python
import pydoof
pydoof.token = "b8bcb..."
pydoof.management_url = "https://eu1-api.doofinder.com"
pydoof.search_url = "https://eu1-search.doofinder.com"

# Lists your search engines
search_engines = pydoof.search_engines.list()

# Search a term in one search engine
result = pydoof.search.query("abe16c8...", "some terms")
```
### Per-request Configuration
You can configure individual requests via keywords arguments. For instance, setting a different token:

```python
# List a search engine indices
pydoof.indices.list("abe16c8...", "product", token="cc83a..")

# Search suggestions for some terms
result = pydoof.search.suggest("cb12b...", "query", search_url = "https://eu1-search.doofinder.com")
```
### Management and Search APIs

PyDoof includes clients for Doofinder management and search APIs. These two clients can work as separated modules. For instance, if you only want to use management API, you do not need to configure the `pydoof.search_url` parameter.

#### Management API
Management API allows you to handle search engines, indices and items. For instance, you can create an index for a search engine and index an item:

```python
import pydoof
pydoof.token = "b8bcb..."
pydoof.management_url = "https://eu1-api.doofinder.com"

# Create an index
index = {
  "options": {
    "exclude_out_of_stock_items": False,
    "group_variants": False
  },
  "name": "product",
  "preset": "product"
}
pydoof.indices.create(hashid="abe16c8...", index=index)

# Index an item
item = {
  "categories": [
    "cat1",
    "cat2"
  ],
  "df_manual_boost": 1,
  "id": "1234",
  "link": "http://www.example.com/img/1234.png",
  "title": "Item Title"
}
pydoof.items.create(hashid="abe16c8...", name="product", item = item)
```
For a complete API reference, see the [Management API docs](https://docs.doofinder.com/api/management/v2/index.html).

#### Search API
Search API allows you to do queries to your search engines, and record data about your sales. For instance, you can search _"cars"_ that are _"blue"_ and with a price lower than €20.000.000.
```python
import pydoof
pydoof.token = "b8bcb..."
pydoof.search_url = "https://eu1-search.doofinder.com"

# Search "cars" that are "blue" and with a price lower than €20.000.000
pydoof.search.query(
	hashid="abe16c8...",
	query="cars",
	filter_={"color": "blue"},
	exclude={"price": {"gt": 20000000}
)
```
And after that, record your sale:
```python
# Add product to cart
pydoof.search_stats.add_to_cart(
	hashid="abe16c8...",
	index_name="product",
	session_id="4affa6",
	item_id="Ref001",
	amount=1,
	title="Ford Fiesta",
	price=8900
)

# And record that sale
pydoof.search_stats.checkout(hashid="abe16c8...", session_id="4affa6")
```

For a complete API reference, see the [Search API docs](https://docs.doofinder.com/api/search/v5/index.html).
