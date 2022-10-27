from django.http import JsonResponse
from psycopg2 import IntegrityError
from rest_framework import generics, permissions
from .serializers import ShowAllData, TodoSerializer, TodoToggleCompleteSerializer
from todo.models import Todo
from django.contrib.auth.models import User
from rest_framework.parsers import JSONParser
from rest_framework.authtoken.models import Token
from django.views.decorators.csrf import csrf_exempt


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


# Sign up function:
@csrf_exempt
def signup(request):
    if request.method == 'POST':
        try:
            data = JSONParser().parse(request)

            # at this stage you can change between user and superuser
            user = User.objects.create_superuser(
                username=data['username'], email=data['email'], password=data['password'])

            # user = User.objects.create_user(
            #     username=data['username'], email=data['email'], password=data['password'])
            user.save()
            token = Token.objects.create(user=user)
            # if user == User.user:
            #     status = 201
            # else:
            #     status = 200
            return JsonResponse({'token_sent_by_server_as_TokenAuth': str(token)}, status=201)
        except IntegrityError:
            return JsonResponse({'error': 'username already taken chanage another one!'}, status=400)
