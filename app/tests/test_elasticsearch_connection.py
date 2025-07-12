from services.elasticsearch import get_elasticsearch_client

def test_elasticsearch_ping():
    assert get_elasticsearch_client().ping()