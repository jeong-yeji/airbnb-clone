from django.utils import timezone
from django.shortcuts import render
from django.views.generic import ListView
from . import models

# Create your views here.

class HomeView(ListView):

    """ HomeView Definition """

    model = models.Room
    paginate_by = 10
    paginate_orphans = 5
    ordering = "created"
    context_object_name = "rooms"

    def get_context_date(self, **kwargs):
        context = super().get_context_date(**kwargs)
        now = timezone.now()
        context["now"] = now
        return context

def room_detail(request, pk):
    return render(request, "rooms/detail.html")