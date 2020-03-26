# Udacity 
## Project SF Crime Statistics with Spark Stream


#### Install
    virtualenv --python=/usr/bin/python3 venv
    . venv/bin/activate
    pip install -r requirements.txt

##### Steps
    sudo apt autoremove
    sudo apt update
    sudo apt upgrade

    sudo apt install scala
    sudo apt install spark
    
    https://kafka.apache.org/quickstart
    tar -xzf kafka_2.12-2.4.1.tgz
    cd kafka_2.12-2.4.1

#### Running
    kafka-2.4.1-src/bin/zookeeper-server-start.sh config/zookeeper.properties
    kafka-2.4.1-src/bin/kafka-server-start.sh config/server.properties
    spark-shell
    spark-submit --packages org.apache.spark:spark-sql-kafka-0-10_2.11:2.4.1 --master local[*] data_stream.py

#### Tests    
    kafka-2.4.1-src/bin/kafka-topics.sh --list --zookeeper localhost:2181
    kafka-2.4.1-src/bin/kafka-console-consumer.sh --topic "udacity.project.sf" --bootstrap-server PLAINTEXT://localhost:9092 --from-beginning

#### Questions
1. How did changing values on the SparkSession property parameters affect the throughput and latency of the data? 

    Changing the sparksession property parameters could change the number of processed rows and the number of available cores
2. What were the 2-3 most efficient SparkSession property key/value pairs? Through testing multiple variations on values, how can you tell these were the most optimal?
    We can monitor the processedRowsPerSecond to find the most optimal configuration of SparkSession.