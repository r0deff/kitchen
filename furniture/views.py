from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect


def index(request): #HttpRequest
    return HttpResponse("Сторінка додатку furniture.")

def categories(request, catid):
    if request.POST:
        print(request.POST)
    return HttpResponse(f"<h1>Статті за категоріями</h1><p>{catid}</p>")

def archive(request, year):
    if int(year) > 2023:
        return redirect('home', permanent=False)
    return HttpResponse(f"<h1>Архів за роками</h1><p>{year}</p>")

def pageNotFound(request, exception):
    return HttpResponseNotFound("<h1>Сторінка не знайдена</h1")



# Create your views here.
