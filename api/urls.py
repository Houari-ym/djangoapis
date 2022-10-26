from django.urls import path
from . import views
urlpatterns = [
    path('todos/', views.TodoList.as_view()),
    path('show/', views.ListAllData.as_view()),
    path('todosU/', views.TodoListCreate.as_view()),
    path('todos/<int:pk>', views.TodoRetrieveUpdateDestroy.as_view()),
    path('todos/<int:pk>/complete', views.TodoToggleComplete.as_view())
]
