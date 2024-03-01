from django.shortcuts import render
from rest_framework import viewsets
from api.models import BlogModel
from api.serializers import BlogSerializer, UserSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.core.serializers import serialize 
import json
# Create your views here.

class BlogViewSet(viewsets.ModelViewSet):
	serializer_class = BlogSerializer
	queryset = BlogModel.objects.all()
	authentication_classes = (TokenAuthentication,)

class UserDetailAPI(APIView):
	authentication_classes = (TokenAuthentication,)
	def get(self,request):
		user = User.objects.get(id=request.user.id)
		serializer = UserSerializer(user)
		return Response(serializer.data)

class UserList(APIView):
	authentication_classes = (TokenAuthentication,)
	def get(self,request):
		user = User.objects.all()
		data = []
		for u in user:
			serializer = UserSerializer(u)
			data.append(serializer.data)
		return Response(data)

class BlogDelete(APIView):
	authentication_classes = (TokenAuthentication,)
	def get(self,request, pk):
		blog = BlogModel.objects.get(id=pk)
		blog.image.delete()
		return Response("success")