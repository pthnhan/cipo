from elasticsearch import Elasticsearch
import pandas as pd
from tabulate import tabulate


def _put(data_folder: str = None, c: int = None, es_obj=None):
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

def _get(es_obj=None, _index:str=None, _id:int=None,):
    res = es.get(index=_index, id=_id, ignore=404)
    print(res)


def _search_keyword(es_obj=None, keyword:str=None):

    list_indexes = [key for key in es.indices.get_alias("*") if "class" in key]
    list_indexes.sort()
    body = {
        "query": { "match": {
            "term": keyword
        }
        },
        "size": 1000
    }
    res = es_obj.search(index=list_indexes, body=body, ignore=400)
    data = []
    if 'hits' in res:
        for x in res['hits']['hits']:
            source = x['_source']
            data.append({'term': source['term'], 'class': source['class']})
    df = pd.DataFrame(data)
    print(tabulate(df, headers='keys', tablefmt='fancy_grid'))

if __name__ == "__main__":
    es = Elasticsearch("https://elasticsearch.pthnhan.online")
    # for c in [1, 9, 36]:
    #     _put_index(data_folder="data",
    #     c = c,
    #     es_obj=es)
    _search_keyword(es_obj=es, keyword="financial")
    # print(es.indices.get_alias("*"))
