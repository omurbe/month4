from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from .views import ClothListView, ClothDetailView, MaleClothListView, FemaleClothListView, KidClothListView, create_review_view

urlpatterns = [
    path("", ClothListView.as_view(), name="cloth_list"),
    path("<int:id>/", ClothDetailView.as_view(), name="cloth_detail"),
    path('male/', MaleClothListView.as_view(), name="male_detail"),
    path('female/', FemaleClothListView.as_view(), name="female_detail"),
    path('kid/', KidClothListView.as_view(), name="kid_detail"),
    path('create_review/', create_review_view, name="create_review"),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)