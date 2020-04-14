from django.shortcuts import render
from tracker.forms import track_covid

import requests

# Create your views here.

def track_covid_data(requests):
        track_data_list = track_covid()
        return render(requests, "tracker/tracker.html", {"track":track_data_list})
