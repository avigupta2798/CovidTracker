from django.shortcuts import render
from home.forms import get_covid

import requests

# Create your views here.

def get_covid_data(requests):
        coviv_data_list = get_covid()
        return render(requests, 'home/home.html', {"covid":coviv_data_list})




'''            {}'age': covdata.GET('agebracket'),
            'backup_notes':covdata.GET('backupnotes'), 
            'current_status':covdata.GET('currentstatus'), 
            'date':covdata.GET('dateannounced'), 
            'city':covdata.GET('detectedcity'), 
            'district':covdata.GET('detecteddistrict'),
            'state':covdata.GET('detectedstate'),  
            'gender': covdata.GET('gender'), 
            'nationality': covdata.GET('nationality'), 
            'notes':covdata.GET('notes'),
            'patient_number':covdata.GET('patientnumber'), 
            'source1': covdata.GET('source1'), 
            'source2':covdata.GET('source2'), 
            'source3':covdata.GET('source3'), 
            'statecode':covdata.GET('statecode'), 
            'status_change_date':covdata.GET('statuschangedate'), 
            'type_of_transmission':covdata.GET('typeoftransmission')}
'''          