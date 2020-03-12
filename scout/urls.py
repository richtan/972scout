from django.urls import path
from . import views

app_name = "scout"
urlpatterns = [
    path('', views.home, name="home"),

    path('input-pit-data', views.pit_data_input, name="pit_data_input"),
    path('input-match-data', views.match_data_input, name="match_data_input"),
    path('rankings', views.rankings, name="rankings"),
    path('team-pages', views.team_pages, name="team_pages"),
]
