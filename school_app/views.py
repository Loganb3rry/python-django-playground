from django.urls import reverse_lazy
from django.views.generic import (TemplateView,
                                  ListView, DetailView,
                                  CreateView, UpdateView, DeleteView)
from school_app import models


class IndexView(TemplateView):
    template_name = 'school_app/index.html'


class SchoolListView(ListView):
    context_object_name = 'schools'
    model = models.School


class SchoolDetailView(DetailView):
    context_object_name = 'school_detail'
    model = models.School
    template_name = 'school_app/school_detail.html'


class SchoolCreateView(CreateView):
    fields = ('name', 'principal', 'location')
    model = models.School


class SchoolUpdateView(UpdateView):
    fields = ('name', 'principal')
    model = models.School


class SchoolDeleteView(DeleteView):
    model = models.School
    success_url = reverse_lazy('school_app:list')
