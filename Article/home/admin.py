from django.contrib import admin

# Register your models here.
from .models import ArticleModel, Profile

admin.site.register(ArticleModel)
admin.site.register(Profile)
