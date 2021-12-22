from django.views.generic import ListView
from django.shortcuts import render
from django.core.management import call_command

from .models import Episode

class HomePageView(ListView):
    model = Episode
    template_name = "homepage.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["episodes"] = Episode.objects.filter().order_by("-pub_date")[:12]
        return context

class Update_List(ListView):
    model = Episode
    template_name = "homepage.html"
    
    def get_context_data(self, **kwargs):
        if ( self.request.method == "GET" ):
            call_command('startjobs')
        context = super().get_context_data(**kwargs)
        context["episodes"] = Episode.objects.filter().order_by("-pub_date")[:12]
        return context

