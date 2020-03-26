from confluent_kafka.admin import AdminClient


def topic_exists(topic):
    """Checks if the given topic exists in Kafka"""
    client = AdminClient({"bootstrap.servers": "PLAINTEXT://localhost:9092"})
    return client.list_topics(timeout=5).topics.get(topic) is not None
    
if __name__ == '__main__':
    if topic_exists('TURNSTILE_SUMMARY'):
        print('exist')
    else:
        print('dont exist')