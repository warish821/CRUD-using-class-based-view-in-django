from django.urls import path
from task_app.views import CreateTask, CreateUser, DeleteTask, ShowTask, UpdateTask


urlpatterns = [

    path('',CreateUser.as_view(),name='create-user'),
    path('create-task/',CreateTask.as_view(),name='create-task'),
    path('show-task/',ShowTask.as_view(),name='show-task'),
    path('update-task/<int:id>',UpdateTask.as_view(),name='update-task'),
    path('delete-task/<int:id>',DeleteTask.as_view(),name='delete-task')
]