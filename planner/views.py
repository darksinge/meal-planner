from django.shortcuts import render, redirect
from django.views.generic import TemplateView


class BaseView(TemplateView):
    pass


class HomeView(BaseView):
    template_name = 'planner/home.html'

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
