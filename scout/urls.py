from django.urls import path
from . import views

app_name = "scout"
urlpatterns = [
    path('', views.HomeView.as_view(), name="home"),
    path('input-pit-data', views.PitDataInputView.as_view(), name="pit_data_input"),
    path('input-match-data', views.MatchDataInputView.as_view(), name="match_data_input"),
    path('pit-data', views.PitDataView.as_view(), name="pit_data"),
    path('match-data', views.MatchDataView.as_view(), name="match_data"),
    path('rankings', views.RankingsView.as_view(), name="rankings"),
    path('team-pages', views.TeamPagesView.as_view(), name="team_pages"),
]
