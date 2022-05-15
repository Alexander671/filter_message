from django.db import models
from django.contrib.auth.models import User

from django.conf import settings

ORDER_STATUS = ((0, 'Review'), (1, 'Blocked'), (2, 'Correct'))

class Messages(models.Model): # Таблица новостей которая наследует models.Model
    message_text = models.TextField(blank=False) # текст сообщения
    date_of_create = models.DateField(auto_now_add=True) # дата создания
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='user_is', on_delete=models.SET_NULL, blank = True, null = True)
    status = models.SmallIntegerField(choices=ORDER_STATUS, default=0) # статус проверки сообщения
    user_to = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='user_to', on_delete=models.SET_NULL, blank = True, null = True)
    class Meta:
        verbose_name = ("Message") # человекочитаемое имя объекта
        verbose_name_plural = ("Messages")  #человекочитаемое множественное 
    def __str__(self):
        return self.message_text  # __str__ применяется для отображения объекта в интерфейсе
