import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'filter_message.settings')
import django
from django.conf import settings

if not settings.configured:
    django.setup()


from messages_service.models import Messages
from messages_service.serializers import MessagesSrializer

import json
from time import sleep

def test():
    from kafka import KafkaConsumer
    consumer = KafkaConsumer('sample', enable_auto_commit=True)
    for message in consumer:
        message = Messages.objects.get(id = message.key)
        if("АБРАКАДАБРА" in message.message_text.upper()):
            message.status = 1
        else:
            message.status = 2

        message.save()        


if __name__ == "__main__":
    test()


