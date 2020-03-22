# from confluent_kafka import avro
# from confluent_kafka.avro import AvroProducer


# def main():

#     value_schema_str = """
#     {
#        "namespace": "my.test",
#        "name": "value",
#        "type": "record",
#        "fields" : [
#          {
#            "name" : "name",
#            "type" : "string"
#          }
#        ]
#     }
#     """

#     key_schema_str = """
#     {
#        "namespace": "my.test",
#        "name": "key",
#        "type": "record",
#        "fields" : [
#          {
#            "name" : "name",
#            "type" : "string"
#          }
#        ]
#     }
#     """

#     value_schema = avro.loads(value_schema_str)
#     key_schema = avro.loads(key_schema_str)
#     value = {"name": "Value"}
#     key = {"name": "Key"}

#     avroProducer = AvroProducer({
#         'bootstrap.servers': 'localhost:9092',
#         'schema.registry.url': 'http://localhost:8081',
#         'debug': 'broker,topic,msg',
#     }, default_key_schema=key_schema, default_value_schema=value_schema)

#     for i in range(5):
#         avroProducer.produce(topic='test', value=value, key=key)
#     avroProducer.flush()


from confluent_kafka import avro
from confluent_kafka.avro import AvroProducer

from models.producer import Producer
import time

def main():

    key_schema = avro.load(f"/home/intelie/code/streaming-data-nanodegree/project_optimizing_public_transportation/producers/models/schemas/arrival_key.json")
    value_schema = avro.load(f"/home/intelie/code/streaming-data-nanodegree/project_optimizing_public_transportation/producers/models/schemas/arrival_value.json")

    p = Producer(
            topic_name="com.test.test",
            key_schema=key_schema,
            value_schema=value_schema, # TODO: Uncomment once schema is defined
            num_partitions=5, # TODO
            num_replicas=1, # TODO
        )
    v = {
        'station_id':666,
        'train_id':'bleble',
        'direction':'bla',
        'line':'blabla',
        'train_status':'bla',
        'prev_station_id':667,
        'prev_direction':'left'
    }
    k = {
        'timestamp': time_millis()
    }
    # for i in range(5):
    p.producer.produce(topic='com.test.test', value=v, key=k)
    p.close()
    # p.producer.flush()


def time_millis():
        """Use this function to get the key for Kafka Events"""
        return int(round(time.time() * 1000))

if __name__ == '__main__':
    main()

# import time
# from pathlib import Path

# from confluent_kafka import avro
# from confluent_kafka.admin import AdminClient, NewTopic
# from confluent_kafka.avro import AvroProducer, CachedSchemaRegistryClient

# from confluent_kafka import Producer


# def main():
#     BROKER_URL = "PLAINTEXT://localhost:9092"
#     TOPIC_NAME = "my-test-test-topic"

#         # TODO: Configure the AdminClient with `bootstrap.servers`
#     #       See: https://docs.confluent.io/current/clients/confluent-kafka-python/#confluent_kafka.admin.AdminClient
#     print(0)
#     client = AdminClient({'bootstrap.servers':BROKER_URL})
#     # TODO: Create a NewTopic object. Don't forget to set partitions and replication factor to 1!
#     #       See: https://docs.confluent.io/current/clients/confluent-kafka-python/#confluent_kafka.admin.NewTopic
#     print(1)
#     topic = NewTopic(TOPIC_NAME, num_partitions=1, replication_factor=1)

#     # TODO: Using `client`, create the topic
#     #       See: https://docs.confluent.io/current/clients/confluent-kafka-python/#confluent_kafka.admin.AdminClient.create_topics
#     print(2)
#     print(client.create_topics([topic]))
#     time.sleep(10)

#     # schema_registry = CachedSchemaRegistryClient("http://schema-registry:8081/")

#     # p = AvroProducer({"bootstrap.servers": BROKER_URL}, schema_registry=schema_registry)
#     print(3)
#     p = Producer({"bootstrap.servers": BROKER_URL})
#     # key_schema = avro.load(f"models/schemas/arrival_key.json")
#     # value_schema = avro.load(f"models/schemas/arrival_value.json")

#     curr_iteration = 0
#     try:
#         while True:
#             # TODO: Produce a message to the topic
#             #       See: https://docs.confluent.io/current/clients/confluent-kafka-python/#confluent_kafka.Producer.produce
#             # p.produce(topic=TOPIC_NAME, key_schema=key_schema, value_schema=value_schema, value=f"Message: {curr_iteration}".encode("utf-8"))
#             p.produce(TOPIC_NAME, f"Message: {curr_iteration}".encode("utf-8"))
#             curr_iteration += 1
#             time.sleep(1)
#             print('produce')
#     except KeyboardInterrupt as e:
#         print("Shutting down")
#     finally:
#         client.delete_topics([topic])

# def test_avro_producer():
#     pass


# if __name__=='__main__':
#     main()


#     schema = avro.loads("""{
#         "type": "record",
#         "name": "click_event",
#         "namespace": "com.udacity.lesson3.exercise4",
#         "fields": [
#             {"name": "email", "type": "string"},
#             {"name": "timestamp", "type": "string"}
#         ]
#     }""")