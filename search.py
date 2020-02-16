from elasticsearch import Elasticsearch
import os

es = Elasticsearch()
index_name = "data"

def search(sentence):
    search_word = sentence

    # 검색
    results = es.search(

        # set index
        index=index_name,

        # 쿼리문
        # multi_match
        body={
            'query': {
                "multi_match": {
                    "query": search_word
                    # "fields": ["name"]
                }
            },
            "size": 30
        }

        # 
    )

    return results['hits']['hits']

    # # 결과
    # if(len(results['hits']['hits']) > 0):
    #     print("--------결과--------")

    #     for result in results['hits']['hits']:
    #         print(f"{result['_source']}")

    #     print("--------결과--------")
    # else:
    #     print("--------없음--------")

while(True):

    searchWord = input(" : ")

    os.system("cls")

    for result in search(searchWord):
        print(result["_source"])