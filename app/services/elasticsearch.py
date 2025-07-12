import logging
import time
from elasticsearch import Elasticsearch
from core.config import settings

logger = logging.getLogger(__name__)

def get_elasticsearch_client():
    return Elasticsearch(hosts=[settings.ELASTICSEARCH_URL])