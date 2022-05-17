# accounts/urls.py
from django.urls import include, path

from .api import CreateUserView

urlpatterns = [
    path('signup/', CreateUserView.as_view(), name='signup'),
    path("", include("rest_framework.urls")),  

]  