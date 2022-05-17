#!/bin/bash

# Start the first process
kafka_2.13-3.1.1/bin/zookeeper-server-start.sh kafka_2.13-3.1.1/config/zookeeper.properties

# Start the second process
kafka_2.13-3.1.1/bin/kafka-server-start.sh kafka_2.13-3.1.1/config/server.properties

# Start the third proccess  
python3 kafka_consumer.py