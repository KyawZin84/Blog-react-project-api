from django.db import models
from django.contrib.auth.models import User
from datetime import datetime 

# Create your models here.
class BlogModel(models.Model):
	id = models.AutoField(primary_key=True)
	header = models.CharField(max_length=100,blank=True)
	body = models.TextField(blank=True)
	image = models.ImageField(default=None,blank=True)
	author = models.ForeignKey(User,on_delete=models.CASCADE,default=None)
	created_at = models.DateTimeField(default=datetime.now,blank=True)

	def __str__(self):
		return self.header

class CommentModel(models.Model):
	id = models.AutoField(primary_key=True)
	content = models.CharField(max_length=100,default=None)
	author = models.ForeignKey(User,on_delete=models.CASCADE,default=None)
	post = models.ForeignKey(BlogModel,on_delete=models.CASCADE,default=None)

	def __str__(self):
		return self.content


	
