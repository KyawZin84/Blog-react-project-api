from rest_framework import serializers
from .models import BlogModel
from django.contrib.auth.models import User

class BlogSerializer(serializers.ModelSerializer):
	class Meta:
		model = BlogModel
		fields = ['id','header','body','image','author','created_at']

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ['id','username','email']

		