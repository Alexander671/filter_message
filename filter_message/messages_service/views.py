
from messages_service.models import Messages
from messages_service.serializers import MessagesConfirmationSrializer, MessagesSrializer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import SessionAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAdminUser, BasePermission, IsAuthenticated
from django.db.models import Q
# Create your views here.

class IsOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.user == request.user or obj.user_to == request.user

class MessageList(APIView):
    serializer_class = MessagesSrializer
    authentication_classes = [JWTAuthentication, SessionAuthentication]
    permission_classes = [IsOwner,  IsAuthenticated]

    def get(self, request, format=None):
        # получать все сообщения мне или от меня
        messages = Messages.objects.all().filter((Q(user=request.user) | Q(user_to=request.user)))
        serializer = MessagesSrializer(messages, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None): # добавляем метод пост,
                                          # чтобы кинуть данные в
                                          # kafka 
                                         
        serializer = MessagesSrializer(data=request.data)
        
        if serializer.is_valid():
            obj = serializer.save(user=self.request.user)
            
            # импорт kafka для подключения
            from kafka import KafkaProducer

            # подключение используем дополнительный сериализатор
            producer = KafkaProducer(bootstrap_servers=['localhost:9092'],key_serializer=str.encode,
                                                                        value_serializer=str.encode,)
            
            # отправляем в кафку
            producer.send('sample', key=str(obj.id), value=obj.message_text)

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


'''
{
    "message_text": 63,
    "status": 2
}
'''

class MessageConfirmationList(APIView):
    permission_classes = (IsAdminUser,)
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

        

