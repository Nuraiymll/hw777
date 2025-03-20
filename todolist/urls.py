from django.urls import path
from .views import TodoListCreateView, TodoDetailView, DeleteAllTodosView

urlpatterns = [
    path("", TodoListCreateView.as_view(), name="todo-list-create"),
    path("<int:pk>/", TodoDetailView.as_view(), name="todo-detail"),
    path("delete_all/", DeleteAllTodosView.as_view(), name="delete-all-todos"),
]