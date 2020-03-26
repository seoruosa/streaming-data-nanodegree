from kafka import KafkaProducer
import json
import time


class ProducerServer(KafkaProducer):

    def __init__(self, input_file, topic, **kwargs):
        super().__init__(**kwargs)
        self.input_file = input_file
        self.topic = topic

    #TODO we're generating a dummy data
    def generate_data(self):
        # https://stackoverflow.com/questions/34010778/python-read-in-an-array-of-json-objects-using-json-loads
        with open(self.input_file, 'r') as f:
            json_data = json.loads(f.read())

        for line in json_data:
            message = self.dict_to_binary(line)
            # TODO send the correct data
            self.send(self.topic, value=message)
            time.sleep(1)

    # TODO fill this in to return the json dictionary to binary
    def dict_to_binary(self, json_dict):
        return json.dumps(json_dict).encode("utf-8")
        