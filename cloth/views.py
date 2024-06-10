from django.shortcuts import render, get_object_or_404
from django.views import generic

from cloth.models import Cloth


# Create your views here
class ClothListView(generic.ListView):
    model = Cloth
    template_name = 'clothes/all_cloth.html'
    context_object_name = 'all_cloth'

    def get_queryset(self):
        return Cloth.objects.order_by('-id')


class ClothDetailView(generic.DetailView):
    template_name = 'clothes/cloth_detail.html'
    context_object_name = 'cloth_id'

    def get_object(self, **kwargs):
        cloth_id = self.kwargs.get('id')
        return get_object_or_404(Cloth, id=cloth_id)


class MaleClothListView(generic.ListView):
    model = Cloth
    template_name = 'clothes/male_cloth.html'
    context_object_name = 'male_cloth'

    def get_queryset(self):
        return Cloth.objects.filter(tags__name='male')


class FemaleClothListView(generic.ListView):
    model = Cloth
    template_name = 'clothes/female_cloth.html'
    context_object_name = 'female_cloth'

    def get_queryset(self):
        return Cloth.objects.filter(tags__name='female')



class KidClothListView(generic.ListView):
    model = Cloth
    template_name = 'clothes/kid_cloth.html'
    context_object_name = 'kid_cloth'

    def get_queryset(self):
        return Cloth.objects.filter(tags__name='kid')
