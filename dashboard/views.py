from django.shortcuts import render
from dashboard.forms import dashboard_covid

import requests

# Create your views here.

def dashboard_covid_data(requests):
        track_data_list = dashboard_covid()
        return render(requests, "dashboard/dashboard.html", {"track":track_data_list})
