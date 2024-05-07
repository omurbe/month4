from django.shortcuts import render
from django.http import HttpResponse
import datetime

def personal_view(request):
    if request.method == 'GET':
        name = "Омурбек"
        surname = "Абдираслов"
        age = "17"
        return HttpResponse(f"Omurbek: {name}<br>Abdirasulov: {surname}<br>17: {age}")

def hobby_view(request):
    if request.method == 'GET':
        hobby = "Volleyball"
        return HttpResponse(f"Валейбол: {hobby}")

def time_view(request):
    if request.method == 'GET':
        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return HttpResponse(f"Текущее время: {now}")