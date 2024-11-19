from elasticsearch import Elasticsearch
es = Elasticsearch('http://localhost:9200')
es.index(index='test_index', id=1, body={'test': 'this is the first test'})
