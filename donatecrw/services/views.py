from django.shortcuts import render, get_object_or_404
from .models import Service, Category
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView


def category(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    return render (request, "services/category.html", {'category':category})


class ServiceListView(ListView):
    model = Service


class ServiceCompletedListView(ListView):
    model = Service

    template_name = 'services/completed_list.html'

class ServiceDetailView(DetailView):
    model = Service

