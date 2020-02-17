from elasticsearch import Elasticsearch
import requests
import pprint

def get(index):
    results = Elasticsearch().indices.get(
        index = index
    )

    return results



if __name__=="__main__":
    index = "data"
    pprint.pprint(get(index))
