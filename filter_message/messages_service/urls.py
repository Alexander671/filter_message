from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from messages_service import views
from .views import MessageConfirmationList, MessageList

urlpatterns = [
    path('message_confirmation/', MessageConfirmationList.as_view(), name='message_confirmation'),
    path('message/', MessageList.as_view(), name='message'),

]

urlpatterns = format_suffix_patterns(urlpatterns)