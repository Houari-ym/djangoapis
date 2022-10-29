from django.urls import path
from . import views
urlpatterns = [
    path('todos/', views.TodoList.as_view()),
    path('show/', views.ListAllData.as_view()),  # Just for play
    path('todosU/', views.TodoListCreate.as_view()),  # just for play
    path('todos/<int:pk>', views.TodoRetrieveUpdateDestroy.as_view()),
    path('todos/<int:pk>/complete', views.TodoToggleComplete.as_view()),
    path('signup/', views.signup, name="sign-up"),
    path('login/', views.login, name="log-in")
]
