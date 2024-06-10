from django.urls import path
from .views import (BlogAdd, BlogChangesView, BlogDeleteView, BlogListView, BlogDetailView)

urlpatterns = [
    path('blog/<int:id>/', BlogDetailView.as_view(), name='blog_detail'),
    path('blog/', BlogListView.as_view(), name='blog_list'),
    path('blog_add/', BlogAdd.as_view(), name='blog_add'),
    path('blog/<int:id>/delete/', BlogDeleteView.as_view(), name='blog_delete'),
    path('blog/<int:id>/update/', BlogChangesView.as_view(), name='blog_change'),

]