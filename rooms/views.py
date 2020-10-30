from django.views.generic import ListView, DetailView
from django.http import Http404
from django.shortcuts import render
from . import models

# Create your views here.

class HomeView(ListView):

    """ HomeView Definition """

    model = models.Room
    paginate_by = 10
    paginate_orphans = 5
    ordering = "created"
    context_object_name = "rooms"

# CBV
class RoomDetail(DetailView):
    
    """ RoomDetail Definition """

    model = models.Room

def search(request):
    city = request.GET.get("city")
    city = str.capitalize(city)
    return render(request, "rooms/search.html", {"city" : city})