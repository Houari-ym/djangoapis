# DjangoApi Labs
## Chapter 11: Authentication – Sign Up

### Basic Authentication:
the most commomn one is HTTP authentication inside the request headers.
- Downsides:
  - The Cridentials are within the request thus cause Security Flow & Vulnerablity.
  -   

### Token authentication:

It uses a generated token from the server-side:
- the client sends a request with usernamme and password to the server to verify that it is authenticated.
- If it is the case, the sever generates a Token and only save that token.
  
1- Setup: 
  inside the 'backend/settings.py' file add :
```python:
INSTALLED_APPS = [
'todo',
'rest_framework',
'api',
'rest_framework.authtoken',
]
``` 

then add the following in the same file:
```python:
REST_FRAMEWORK = {
'DEFAULT_AUTHENTICATION_CLASSES':[
'rest_framework.authentication.TokenAuthentication',
]
}
```
2- User sign up Views and urls :
- add urls.py path 
- add views.py function for the sign up:
```python:
class TodoToggleComplete(generics.UpdateAPIView):

    @csrf_exempt
    def signup(request):
    if request.method == 'POST':
    try:
    data = JSONParser().parse(request) # data is a dictionary
    user = User.objects.create_user(
    username=data['username'],
    password=data['password'])
    user.save()
    token = Token.objects.create(user=user)
    return JsonResponse({'token':str(token)},status=201)
    except IntegrityError:
    return JsonResponse(
    {'error':'username taken. choose another username'},status=400)
```