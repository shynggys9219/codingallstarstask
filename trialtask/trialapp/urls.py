from django.urls import path
from .views import *

app_name = "trialapp"

urlpatterns = [
    path("", home, name="home"),
    path("scrape/", scrape_request, name="scrape"),
    path("download/", download_file, name="download-file"),
    path("getfile/", get_file, name="get_file"),
]
