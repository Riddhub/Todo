from django.urls import path

from todo.views import *

urlpatterns = [
    path("", index, name='index'),
    path("add", addTodo, name='add'),
    path("complete/<note_id>", completeTodo, name='complete'),
    path("deleteCompleted", deleteCompleted, name='deleteCompleted'),
    path("deleteAll", deleteAll, name='deleteAll'),
]