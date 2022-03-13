from django.urls import path

#Getting views
from . import views

app_name = "mainApp"
urlpatterns = [
    path("", views.index, name='index'),
    path("addTask/", views.create_task, name="create-task"),
    path("deleteTask/<int:id>/", views.delete_task, name="delete-task"),
]
