from elasticsearch import Elasticsearch, helpers
import json

def make_index(es, index):
    """인덱스를 신규 생성한다(존재하면 삭제 후 생성) """
    if es.indices.exists(index=index):
        es.indices.delete(index=index)
    es.indices.create(
        index=index,

        body={
            "settings": {
                "analysis": {
                    "analyzer": {
                        # 인덱싱 형태소 분석기
                        "my_analyzer": {
                            "type": "custom",
                            "tokenizer": "standard",
                            "filter": [
                                # cjk_bigram : bigram 단위로 토큰화
                                "cjk_bigram"
                            ]
                        },
                        # 검색어 형태소 분석기
                        "my_stop_analyzer": {
                            "type": "custom",
                            "tokenizer": "standard",
                            "filter": [
                                "cjk_bigram"
                            ]
                        }
                    }
                }
            },
            # "settings": {
            #     "analysis": {
            #         "analyzer": {
            #             "my_analyzer": {
            #                 "type": "custom",
            #                 "tokenizer": "nori_discard",
            #                 "filter": [
            #                     "korean_shingle"
            #                 ]
            #             },
            #             "my_stop_analyzer": {
            #                 "type": "custom",
            #                 "tokenizer": "nori_discard",
            #                 "filter": [
            #                     "korean_shingle"
            #                 ]
            #             }
            #         },
            #         "tokenizer" : {
            #             "nori_discard" : {
            #                 "type" : "nori_tokenizer",
            #                 "decompound_mode" : "mixed"
            #             }
            #         },
            #         "filter": {
            #             # custom filter shingle
            #             "korean_shingle": {
            #                 "type": "shingle",
            #                 "token_separator": '',
            #                 "max_shingle_size" : 3
            #             },
            #             "korean_bigrams_filter": {
            #                 "type": "cjk_bigram",
            #                 "ignored_scripts": [
            #                     "han",
            #                     "hiragana",
            #                     "katakana"
            #                 ],
            #                 "output_unigrams": True
            #             }
            #         }
            #     }
            # },
            "mappings": {
                "properties": {
                    "name": {
                        "type": "text",
                        "analyzer": "my_analyzer",
                        "search_analyzer": "my_stop_analyzer",
                        "search_quote_analyzer": "my_analyzer"
                    },
                    "category": {
                        "type": "text",
                        "analyzer": "my_analyzer",
                        "search_analyzer": "my_stop_analyzer",
                        "search_quote_analyzer": "my_analyzer"
                    },
                    "text": {
                        "type": "text",
                        "analyzer": "my_analyzer",
                        "search_analyzer": "my_stop_analyzer",
                        "search_quote_analyzer": "my_analyzer"
                    }
                }
            }

        }
    )

if __name__=="__main__":
    # default is localhost:9200
    es = Elasticsearch()

    index_name = "data"
    make_index(es, index_name)

    with open("data.json", 'r', encoding='utf-8') as json_file:
        helpers.bulk(es, json.load(json_file))
