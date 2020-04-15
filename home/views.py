from django.shortcuts import render
from home.forms import get_covid

import requests

# Create your views here.

def get_covid_data(requests):
        coviv_data_list = get_covid()
        return render(requests, 'home/home.html', {"covid":coviv_data_list})       