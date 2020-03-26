from kafka import KafkaConsumer
import json

class ConsumerServer(KafkaConsumer):
    def __init__(self, topic, **kwargs):
        super().__init__(**kwargs)
        self.topic = topic
    
    def consumer(self):
        return self

if __name__ == '__main__':
    consumer = KafkaConsumer("udacity.project.sf", 
                            bootstrap_servers="localhost:9092", 
                            value_deserializer=lambda m: json.loads(m.decode('ascii')),
                            consumer_timeout_ms=10000 #10s
                            )
    try:
        for message in consumer:
            print(message.value)
    except KeyboardInterrupt:
        print("\nConsumer Finished")
    
    consumer.close()