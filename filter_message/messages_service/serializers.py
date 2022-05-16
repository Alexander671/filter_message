from rest_framework import serializers
from .models import Messages

class MessagesSrializer(serializers.ModelSerializer):
        class Meta:
                model = Messages
                fields = ('message_text','user_to')
                extra_kwargs = {'message_text': {'required': False},'user_to': {'required': False}}

class MessagesConfirmationSrializer(serializers.ModelSerializer):
        class Meta:
                model = Messages
                fields = ('message_text','user_to', 'status')
