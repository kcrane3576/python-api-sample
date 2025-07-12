import time
from elasticsearch import Elasticsearch
from core.config import settings

def get_elasticsearch_client():
    return Elasticsearch(hosts=[settings.ELASTICSEARCH_URL])