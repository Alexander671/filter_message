from email.message import Message
from .models import Messages
from rest_framework import viewsets, permissions
from .serializers import MessagesSrializer


class MessageViewSet(viewsets.ModelViewSet):
    queryset = Messages.objects.all()
    permissions_classes = [
        permissions.AllowAny
    ]
    serializer_class = MessagesSrializer