from django.urls import path
from . import views

app_name = "publicity"
urlpatterns = [
    path('', views.home, name="home"),
]
