from django.shortcuts import render
from home.forms import CovidForm
from home.models import *
import requests

# Create your views here.

def get_covid_data(requests):
        coviv_data_list = Covid.objects.values()
        return render(requests, 'home/home.html', {"covid":coviv_data_list})       