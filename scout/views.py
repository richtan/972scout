from django.shortcuts import render, redirect
from .forms import *

def home(request):
    return render(request, "scout/home.html")

def rankings(request):
    return redirect("https://www.thebluealliance.com/event/2019casf#rankings", permanent=True)

def team_pages(request):
    return render(request, "scout/team_pages.html")

def pit_data_input(request):
    form = PitInputForm(request.POST or None)
    if form.is_valid():
        form.save()
    return render(request, "scout/pit_data_input.html", {"form": form})

def match_data_input(request):
    form = MatchInputForm(request.POST or None)
    if form.is_valid():
        form.save()
    return render(request, "scout/match_data_input.html", {"form": form})
