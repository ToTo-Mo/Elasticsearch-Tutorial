from elasticsearch import Elasticsearch

def analyze(sentence):
    results = Elasticsearch().indices.analyze(
        index = "data",
        body={
            "analyzer": "my_analyzer",
            "text": sentence
        }
    )
    print([key["token"] for key in results["tokens"]])

while(True):
    analyze(input(" : "))
