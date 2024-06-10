from django.contrib import admin
from .models import Cloth, TagCloth, Review

# Register your models here.
admin.site.register(Cloth)
admin.site.register(TagCloth)
admin.site.register(Review)
