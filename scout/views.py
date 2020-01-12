from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView
from .forms import *

class HomeView(TemplateView):
    template_name = "scout/home.html"

class PitDataInputView(FormView):
    template_name = "scout/pit_data_input.html"
    form_class = PitInputForm

class MatchDataInputView(FormView):
    template_name = "scout/match_data_input.html"
    form_class = MatchInputForm

class PitDataView(TemplateView):
    template_name = "scout/pit_data.html"

class MatchDataView(TemplateView):
    template_name = "scout/match_data.html"

class RankingsView(TemplateView):
    template_name = "scout/rankings.html"

class TeamPagesView(TemplateView):
    template_name = "scout/team_pages.html"
