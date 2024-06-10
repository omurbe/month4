from django.views import generic
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
import datetime

from .forms import BlogForm
from .models import BlogModels


def BlogModels_view(request):
    if request.method == 'GET':
        posts = BlogModels.objects.all()
        return render(request, template_name='blog.html', context={'posts': posts})


def Blog_vews_detail_view(request, id):
    if request.method == 'GET':
        post = get_object_or_404(BlogModels, id=id)
        return render(request, template_name='blog_detail.html', context={'post': post})


class BlogChangesView(generic.UpdateView):
    template_name = 'blog_change.html'
    form_class = BlogForm
    success_url = '/blog/'

    def get_object(self, **kwargs):
        blog_id = self.kwargs.get('id')
        return get_object_or_404(BlogModels, id=blog_id)

    def form_valid(self, form):
        return super(BlogChangesView, self).form_valid(form=form)


class BlogDeleteView(generic.DeleteView):
    template_name = 'blog_delete.html'
    success_url = '/blog/'

    def get_object(self, **kwargs):
        blog_id = self.kwargs.get('id')
        return get_object_or_404(BlogModels, id=blog_id)


class BlogAdd(generic.CreateView):
    template_name = 'blog_add.html'
    form_class = BlogForm
    success_url = '/blog/'

    def form_valid(self, form):
        return super(BlogAdd, self).form_valid(form=form)





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