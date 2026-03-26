from elasticsearch import Elasticsearch

es = Elasticsearch("http://localhost:9200")

def index_log(msg):
    es.index(index="logs", document={"msg": msg})

def search_logs(q):
    return es.search(index="logs", query={"match": {"msg": q}})