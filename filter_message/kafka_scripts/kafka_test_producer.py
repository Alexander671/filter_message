from time import sleep
from kafka import KafkaProducer
from json import dumps
from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                         value_serializer=lambda x: 
                         dumps(x).encode('utf-8'))

data = {'number' : 1}
producer.send('sample', value=data)
sleep(5)