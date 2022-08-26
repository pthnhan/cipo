# from elasticsearch import Elasticsearch
# import pandas as pd

# if __name__ == "__main__":
#     es = Elasticsearch("https://elasticsearch.pthnhan.online")
#     df = pd.read_csv("/mnt/d/work/cipo/data/ca_tm_good_services_term_1000.csv")
#     doc_list = df.to_dict('records')
#     for doc in doc_list[:100]:
#         print(doc)
#         es.index(index=f"cipo-ca_tm_goods_services_term", body=doc_list[0])
    

