from django.urls import path
from .views import (personal_view, hobby_view, time_view, Blog_vews_detail_view, BlogModels_view,
                    BlogAdd, BlogChangesView, BlogDeleteView)

urlpatterns = [
    path('personal/', personal_view, name='personal'),
    path('hobby/', hobby_view, name='hobby'),
    path('time/', time_view, name='time'),
    path('blog/<int:id>/', Blog_vews_detail_view, name='blog_detail'),
    path('blog/', BlogModels_view, name='blog_list'),
    path('blog_add/', BlogAdd.as_view(), name='blog_add'),
    path('blog/<int:id>/delete/', BlogDeleteView.as_view(), name='blog_delete'),
    path('blog/<int:id>/update/', BlogChangesView.as_view(), name='blog_change'),

]