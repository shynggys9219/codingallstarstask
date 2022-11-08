from django.shortcuts import render, redirect
from .async_scrapper import scrapper_main, settings
from django.http import HttpResponse, Http404
import os

# Create your views here.

CATEGORIES = ['data-science', 'business', 'computer-science', 'personal-development', 'social-sciences',
              'arts-and-humanities']


def home(request):
    return render(request, "trialapp/home.html", context={"categories": CATEGORIES})


def scrape_request(request):
    if request.method == "POST":
        if request.POST:
            category = request.POST.get("cats")
            print(category)
            scrapper_main(category)
    return redirect("trialapp:download-file")


def download_file(request):
    files_list = os.listdir(f"{settings.MEDIA_ROOT}/files/")
    return render(request, "trialapp/download.html", context={"files": files_list})


def get_file(request):
    if request.method == "POST":
        print(request.POST)
        filename = request.POST.get("filename")
        filepath = fr"{settings.MEDIA_ROOT}\files\{filename}"
        print(filepath)
        if os.path.exists(filepath):
            with open(filepath, 'rb') as fh:
                response = HttpResponse(fh.read(), content_type="application/vnd.ms-excel")
                response['Content-Disposition'] = 'inline; filename=' + os.path.basename(filepath)
                return response
    raise Http404
