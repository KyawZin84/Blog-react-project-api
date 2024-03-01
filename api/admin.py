from django.contrib import admin
from .models import BlogModel
from .models import CommentModel
# Register your models here.

admin.site.register(BlogModel)
admin.site.register(CommentModel)
