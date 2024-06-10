from django.views import generic
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
import datetime

from .forms import BlogForm
from .models import BlogModels


class BlogListView(generic.ListView):
    template_name = 'blog.html'
    context_object_name = 'posts'
    model = BlogModels

class BlogDetailView(generic.ListView):
    template_name = 'blog_detail.html'
    context_object_name = 'post'
    model = BlogModels


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


class SearchBlogView(generic.ListView):
    template_name = 'blog.html'
    context_object_name = 'blogs'
    paginate_by = 5

    def get_queryset(self):
        return BlogModels.objects.filter(name__icontains=self.request.GET.get('q'))

    def get_context_data(self, *, object_list=None, **kwargs):
        contex = super().get_context_data(**kwargs)
        contex['q'] = self.request.GET.get('q')
        return contex
