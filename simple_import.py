from elasticsearch import Elasticsearch, helpers
import json


def make_index(es, index):
    """인덱스를 신규 생성한다(존재하면 삭제 후 생성) """
    if es.indices.exists(index=index):
        es.indices.delete(index=index)
    es.indices.create(index=index)


if __name__=="__main__":
    # default is localhost:9200
    es = Elasticsearch()

    index_name = "data"
    make_index(es, index_name)

    with open("data.json", 'r', encoding='utf-8') as json_file:
        helpers.bulk(es, json.load(json_file))
