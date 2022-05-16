from django.shortcuts import render
from messages_service.models import Messages

from messages_service.serializers import MessagesConfirmationSrializer, MessagesSrializer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from json import dumps
from time import sleep

from pickle import dumps,HIGHEST_PROTOCOL

# Create your views here.
class MessageList(APIView):
    def get(self, request, format=None):
        messages = Messages.objects.all()
        serializer = MessagesSrializer(messages, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None): # добавляем метод пост,
                                          # чтобы кинуть данные в
                                          # kafka 
                                          
        serializer = MessagesSrializer(data=request.data)
        
        if serializer.is_valid():
            obj = serializer.save()
            
            # импорт kafka для подключения
            from kafka import KafkaProducer

            # подключение используем дополнительный сериализатор
            producer = KafkaProducer(bootstrap_servers=['localhost:9092'],key_serializer=str.encode,
                                                                        value_serializer=str.encode,)
            
            # отправляем в кафку
            producer.send('sample', key=str(obj.id), value=obj.message_text)

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MessageConfirmationList(APIView):
    
    def post(self, request, format=None): # здесь получаем status и изменяем его
        
        # получили данные из запроса
        message_id = request.data['message_id']
        status1 = request.data['status']
        
        # получили объект
        message = Messages.objects.get(pk=message_id)
        
        # создали сериализатор
        serializer = MessagesConfirmationSrializer(message, data={'status' : status1}, partial=True)

        # верифицировали
        if serializer.is_valid():
            serializer.save()
            print(serializer.data)

            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        

