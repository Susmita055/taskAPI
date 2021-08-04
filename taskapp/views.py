from rest_framework.generics import GenericAPIView
from taskapp.models import Register
from django.http.response import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate,login
from .forms import RegisterForm
from .models import Task
from .serializer import TaskSerializser
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import jwt,json
from rest_framework import serializers, views
from rest_framework.response import Response
from django.contrib.auth.models import User
# Create your views here.




#pip install PyJWT
def register(request):
    if request.method=='POST':
        firstname=request.POST['FirstName']
        lastname=request.POST['LastName']
        email = request.POST['Email']
        password = request.POST['Password']
        register=Register.objects.create(FirstName=firstname,LastName=lastname,Email=email,Password=password)
        user = User.objects.create_user(username= email,email= email,password= password)    
        user.save()
        return HttpResponse("registered")
    else:
        form= RegisterForm()
    return render(request,'registration.html', {'form':form})

class Login(views.APIView):

    def post(self, request, *args, **kwargs):
        if not request.data:
            return Response({'Error': "Please provide username/password"}, status="400")
        
        email = request.data['username']
        password = request.data['password']
        user=authenticate(request, username=email, password=password)
        
        
        print(email)
        print(password)
        try:
            user = User.objects.get(username=email)
            print(user)
        except User.DoesNotExist:
            return Response({'Error': "Invalid username/password"}, status="400")
        if user:
            
            payload = {
                'id': user.id,
                'email': user.email,
            }
            jwt_token = {'token': jwt.encode(payload, "SECRET_KEY")}

            return HttpResponse(
              json.dumps(jwt_token),
              status=200,
              content_type="application/json",
              
            )
            login(emial, password)
        else:
            return Response(
              json.dumps({'Error': "Invalid credentials"}),
              status=400,
              content_type="application/json"
            )





class TaskList(APIView):
    authentication_classes = []
    permission_classes = []
    
    def get(self, request, format=None):
        tasks = Task.objects.all()
        serializer = TaskSerializser(tasks, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = TaskSerializser(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class taskDetail(APIView):
  
    def get_object(self, pk):
        try:
            return Task.objects.get(pk=pk)
        except Task.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        task = self.get_object(pk)
        serializer = TaskSerializser(task)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        task = self.get_object(pk)
        serializer = TaskSerializser(task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        task = self.get_object(pk)
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)