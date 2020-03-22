 
 ### Installation of docker
    sudo dpkg -i docker-ce_18.09.4_3-0_ubuntu-bionic_amd64.deb 
    sudo dpkg -i docker-ce-cli_18.09.4_3-0_ubuntu-bionic_amd64.deb 
    sudo dpkg -i docker-ce_18.09.4_3-0_ubuntu-bionic_amd64.deb


### Docker commands
    sudo systemctl restart docker.service
    sudo service docker restart
    sudo service docker status
    docker ps -a
    docker start projectoptimizingpublictransportation_schema-registry_1





#### Connect
docker exec -it projectoptimizingpublictransportation_connect_1 /bin/bash
kafka-topics --list --zookeeper zookeeper:2181
kafka-topics --delete --zookeeper zookeeper:2181 --topic com.udacity.*


#### Kafka
docker exec -it projectoptimizingpublictransportation_kafka0_1 /bin/bash
kafka-topics --list --zookeeper zookeeper:2181
kafka-console-producer --topic "my-first-topic" --broker-list PLAINTEXT://kafka0:9092
kafka-console-consumer --topic "my-test-test-topic" --bootstrap-server PLAINTEXT://kafka0:9092 --from-beginning



#### Running Simulation
virtualenv --python=/usr/bin/python3 venv
. venv/bin/activate
pip install -r requirements.txt


#### Schema Registry

curl -X GET http://localhost:8081/subjects
curl -X DELETE http://localhost:8081/subjects/com.udacity.station.arrivals-value

#### KSQL

curl -sX GET "http://localhost:8088/info"
curl -sX GET "http://localhost:8088/healthcheck"

#### GIT SSH KEY

eval "$(ssh-agent -s)"
ssh-add ~/.ssh/private_key
ssh -T git@github.com