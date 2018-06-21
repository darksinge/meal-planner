from django.http import HttpResponse
from django.views.generic import TemplateView

class BaseView(TemplateView):
    template_name = 'planner/home.html'