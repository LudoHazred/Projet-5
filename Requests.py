import requests
import json

payload = {
    'action': 'process',
    'tagtype_0': 'categories',
    'tag_contains_0': 'contains',
    'tag_0': '', #parameters to choose
    'sort_by': 'unique_scans_n',
    'page_size': 100,
    'countries': 'France',
    'json': 1,
    'page': 1,
    }

r = requests.get('https://fr.openfoodfacts.org/cgi/search.pl', params=payload)

r.json()
