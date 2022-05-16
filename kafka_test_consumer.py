
from requests import post
import json

def test():

    # получили консьюмером данные
    # из кафки
    from kafka import KafkaConsumer
    consumer = KafkaConsumer('sample', enable_auto_commit=True, value_deserializer=lambda m: m.decode('utf-8'),
                                                                key_deserializer=lambda m: m.decode('utf-8'))
    for message in consumer:
        
        print(message.value)
        
        true_false = "АБРАКАДАБРА" in message.value.upper()
        status = 1 if true_false else 2

        # создаем два запроса
        # true/false
        r = post('http://127.0.0.1:8000/api/message_confirmation/', data={'message_id': message.key, 'status' : status})
        print(r)


if __name__ == "__main__":
    test()


