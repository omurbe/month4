from django.contrib import admin
from .models import BlogModels, Review

# Register your models here.
admin.site.register(BlogModels)
admin.site.register(Review)

