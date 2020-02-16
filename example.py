from elasticsearch import Elasticsearch, helpers
import json

# default is localhost:9200
es_client = Elasticsearch()

index_name = "wisesaying"

body = {
    "quote": "자신을 화나게 했던 행동을 다른 이에게 행하지 말라. ",
    "name": "소크라테스",
    "category": "공부"
}

result = es_client.index(index=index_name, body=body)
print(result)

# result = es_client.search(
#     index=index_name,

#     body={
#         "query" : {
#             "multi_match":{
#                 "query" : "자신을 화나게 했던"
#             }
#         },
#         "size" : 30
#     }
# )

# for doc in result["hits"]['hits']:
#     print(doc["_source"])