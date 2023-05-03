from django.urls import path

from todo.views import *

urlpatterns = [
    path("", index, name='index'),
]