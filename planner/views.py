from django.shortcuts import render
from django.views.generic import TemplateView


class BaseView(TemplateView):
    pass


class HomeView(BaseView):
    template_name = 'planner/home.html'
