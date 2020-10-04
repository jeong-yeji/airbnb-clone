from math import ceil
from django.shortcuts import render
from . import models

# Create your views here.

def all_rooms(request):
    page = request.GET.get("page", 1) # request가 없는 경우 > default 값 1
    page = int(page or 1) # page값이 비워져있는 경우 오류 발생 > default값으로 1 주기
    page_size = 10
    limit = page_size * page
    offset = limit - page_size
    all_rooms = models.Room.objects.all()[offset:limit]
    page_count = ceil(models.Room.objects.count() / page_size)
    return render(
        request,
        "rooms/home.html",
        {
            "rooms": all_rooms,
            "page": page,
            "page_count": page_count,
            "page_range": range(0, page_count),
        },
    )