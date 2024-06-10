from django import forms

from blog.models import BlogModels


class BlogForm(forms.ModelForm):
    class Meta:
        model = BlogModels
        fields = '__all__'