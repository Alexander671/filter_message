
from requests import post
import json


import environ # Initialise environment variables
env = environ.Env()
environ.Env.read_env('filter_message/filter_message/.env')

HOST_SERVER = env('HOST_SERVER')
LOGIN = env('LOGIN')
PASSWORD = env('PASSWORD')


def test():

    # jwt auth
    # не доделано, должен обновляться,
    # а не новый каждый раз
    r_auth = post(f'{HOST_SERVER}api/token/', json={'username': LOGIN, 'password' : PASSWORD})
    token = format(r_auth.json()['access'])


    # получили консьюмером данные
    # из кафки
    from kafka import KafkaConsumer
    consumer = KafkaConsumer('sample', enable_auto_commit=True, value_deserializer=lambda m: m.decode('utf-8'),
                                                                key_deserializer=lambda m: m.decode('utf-8'))
    for message in consumer:

        # проверка статуса    
        true_false = "АБРАКАДАБРА" in message.value.upper()
        status = 1 if true_false else 2

        # создаем запрос 1/2
        # headers - token jwt 
        # headers - application/json
        r = post(f'{HOST_SERVER}api/message_confirmation/',
                  json={'message_id': message.key, 'status' : status},
                  headers={'Authorization': f'Bearer {token}'})
        print(r.json())


if __name__ == "__main__":
    test()


