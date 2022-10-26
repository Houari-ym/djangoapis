from rest_framework import generics, permissions
from .serializers import ShowAllData, TodoSerializer, TodoToggleCompleteSerializer
from todo.models import Todo


class TodoList(generics.ListAPIView):
    serializer_class = TodoSerializer

    def get_queryset(self):
        user = self.request.user
        return Todo.objects.filter(user=user).order_by('created')
# The above is only for ReadOnly Access  ----METHOD 1---


# Try to be deleted
class ListAllData(generics.ListAPIView):
    serializer_class = ShowAllData

    def get_queryset(self):
        user = self.request.user
        return Todo.objects.all()

# This is for ReadWrite Access ----METHOD 2---


class TodoListCreate(generics.ListCreateAPIView):
    serializer_class = TodoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Todo.objects.filter(user=user).order_by('-created')


class TodoRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TodoSerializer
    persmission = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user

        return Todo.objects.filter(user=user)


# Update:
class TodoToggleComplete(generics.UpdateAPIView):
    serializer_class = TodoToggleCompleteSerializer
    permission = [permissions.IsAuthenticated]

    def get_queryset(self): 
        user = self.request.user
        return Todo.objects.filter(user=user)

    def perform_update(self, serializer):
        serializer.instance.completed = not(serializer.instance.completed)
        serializer.save()
