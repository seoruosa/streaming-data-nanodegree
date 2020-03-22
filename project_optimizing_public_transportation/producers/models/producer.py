"""Producer base-class providing common utilites and functionality"""
import logging
import time


from confluent_kafka import avro
from confluent_kafka.admin import AdminClient, NewTopic
from confluent_kafka.avro import AvroProducer

logger = logging.getLogger(__name__)


class Producer:
    """Defines and provides common functionality amongst Producers"""

    # Tracks existing topics across all Producer instances
    existing_topics = set([])
    # BROKER_URL = 'http://kafka0:9092'
    BROKER_URL = 'localhost:9092'
    SCHEMA_REGISTRY_URL = "http://localhost:8081"
    # SCHEMA_REGISTRY_URL = "http://schema-registry:8081/"

    def __init__(
        self,
        topic_name,
        key_schema,
        value_schema,
        num_partitions=1,
        num_replicas=1,
    ):
        """Initializes a Producer object with basic settings"""
        self.topic_name = topic_name
        self.key_schema = key_schema
        self.value_schema = value_schema
        self.num_partitions = num_partitions
        self.num_replicas = num_replicas

        #
        #
        # TODO: Configure the broker properties below. Make sure to reference the project README
        # and use the Host URL for Kafka and Schema Registry!
        #
        
        self.broker_properties = {
            'bootstrap.servers': self.BROKER_URL,
            'schema.registry.url': self.SCHEMA_REGISTRY_URL,
            # 'debug': 'broker,topic,msg',
            'on_delivery': lambda err, report: logger.debug(f"succesfully delivered report"),
            # TODO
        }

        # If the topic does not already exist, try to create it

        if self.topic_name not in Producer.existing_topics:
            self.create_topic()
            Producer.existing_topics.add(self.topic_name)

        # TODO: Configure the AvroProducer
        self.producer = AvroProducer(
            self.broker_properties,
            default_key_schema=key_schema, 
            default_value_schema=value_schema
        )

    def __str__(self):
        return f"{self.producer} {self.BROKER_URL}"

    def create_topic(self):
        """Creates the producer topic if it does not already exist"""
        #
        #
        # TODO: Write code that creates the topic for this producer if it does not already exist on
        # the Kafka Broker.
        # if not hasattr(self, 'client'):
        client = AdminClient({
            'bootstrap.servers': self.broker_properties['bootstrap.servers']
        })
        new_topics = [NewTopic(
            topic=self.topic_name,
            num_partitions=self.num_partitions,
            replication_factor=self.num_replicas,
        )]
        fs = client.create_topics(new_topics)

        for topic, f in fs.items():
            try:
                f.result()  # The result itself is None
                print(f"Topic {topic} created")
            except Exception as e:
                print(f"Failed to create topic {topic}: {e}")
#         check if the Kafka Broker dont have a topic with this name


#         if client.list_topics(timeout=5).topics.get(self.topic_name) is None:   
        # if self.topic_name not in Producer.existing_topics:
        #     topic = NewTopic(self.topic_name, num_partitions=self.num_partitions, replication_factor=self.num_replicas)
        #     client.create_topics([topic])
        # else:
        #     logger.info("Topic already exists")
        #
#         logger.info("topic creation kafka integration incomplete - skipping")

    def time_millis(self):
        return int(round(time.time() * 1000))

    def close(self):
        """Prepares the producer for exit by cleaning up the producer"""
        #
        #
        # TODO: Write cleanup code for the Producer here
        #
        # client = AdminClient({'bootstrap.servers': self.BROKER_URL})
        # if len(Producer.existing_topics)>0:
        #     delete_answer = client.delete_topics(list(Producer.existing_topics))
        # logger.info(f"cleanup code for Producer {delete_answer}")
        # logger.info("producer close incomplete - skipping")
        # del self
        logger.debug('closeeeee')
        if self.producer is not None:
            logger.debug("flushing producer...")
            self.producer.flush()

    def time_millis(self):
        """Use this function to get the key for Kafka Events"""
        return int(round(time.time() * 1000))
