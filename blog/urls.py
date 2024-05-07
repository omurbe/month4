from django.urls import path
from .views import personal_view, hobby_view, time_view

urlpatterns = [
    path('personal/', personal_view, name='personal'),
    path('hobby/', hobby_view, name='hobby'),
    path('time/', time_view, name='time')
]