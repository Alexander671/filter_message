#!/bin/bash


# Function that will get executed when the user presses Ctrl+C
function handler(){
    echo "Processing the Ctrl+C"
    docker-compose restart
    sudo kill -9 `sudo lsof -t -i:8000`
    sudo kill -9 `sudo lsof -t -i:2181`
    sudo kill -9 `sudo lsof -t -i:9092`

}

# Start the first process
 python3 manage.py runserver 0.0.0.0:8000 &


# Start the second process
(sleep 5; kafka_2.13-3.1.1/bin/zookeeper-server-start.sh kafka_2.13-3.1.1/config/zookeeper.properties)  &

# Start the third proccess  
(sleep 15; kafka_2.13-3.1.1/bin/kafka-server-start.sh kafka_2.13-3.1.1/config/server.properties) &

# Start the fourth proccess  
(sleep 25; python3 kafka_consumer.py) &

sleep 60


#Wait for any process to exit
wait -n




# Exit with status of process that exited first
exit $?