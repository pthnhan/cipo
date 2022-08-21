from datetime import datetime
import json
from elasticsearch import Elasticsearch
import pandas as pd


def _put_index(data_folder: str = None, c: int = None, es_obj=None):
    df = pd.read_excel(f"{data_folder}/class{c}.xls", header=0, skiprows=[0])
    df = df[df.Status == 'Active']
    term = df.Term.to_list()
    for i in range(len(term)):
        print(f"class {c}, {i}, {term[i]}")
        doc = {
            "term": term[i],
            "class": c,
            "statement": ""
        }
        es_obj.index(index=f"class{c}", id=i+1, body=doc)

def _get_index(es_obj=None):
    res = es.get(index="class1", id=500, ignore=404)
    print(res)



if __name__ == "__main__":
    es = Elasticsearch("https://elasticsearch.pthnhan.online")
    # for c in [1, 9, 36]:
    #     _put_index(data_folder="data",
    #     c = c,
    #     es_obj=es)
    _get_index(es)

# doc = {
#     'a': {
#     'author': 'author_name_a',
#     'text': 'ABCHakchwakucSAJAKHKJXHS',
#     'timestamp': datetime.now(),
# },
# 'b':
# {
#     'author': 'author_name_b',
#     'text': 'ABCHSAJAKHKJXHSafhcanas',
#     'timestamp': datetime.now(),
# }
# }
# res = es.index(index="test-index", id=3, body=doc)
# print(res['result'])

# res = es.get(index="test-index", id=2)
# print(res)

# res = es.search(index="test-index", body={'query': {"match_all": {}}})
# print("Got %d Hits:" % res['hits']['total']['value'])

# print(res)