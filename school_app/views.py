from django.shortcuts import render
from django.views.generic import View, TemplateView, ListView, DetailView
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
