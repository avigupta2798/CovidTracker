"""
Import Json data from an api to Database
"""

import requests
import pandas as pd
from home.models import Covid
import datetime
from django.core.management.base import BaseCommand

IMPORT_URL = 'https://api.covid19india.org/raw_data.json'

class Command(BaseCommand):
    def import_covid_data(self, covdata):
            age = covdata.get('agebracket', None)
            backup_notes = covdata.get('backupnotes', None) 
            current_status = covdata.get('currentstatus', None)
            date_announced = covdata.get('dateannounced', None)
            city = covdata.get('detectedcity', None) 
            district = covdata.get('detecteddistrict', None)
            state = covdata.get('detectedstate', None)
            gender = covdata.get('gender', None)
            nationality = covdata.get('nationality', None) 
            notes = covdata.get('notes', None)
            patient_number = covdata.get('patientnumber', None) 
            source1 = covdata.get('source1', None)
            source2 = covdata.get('source2', None) 
            source3 = covdata.get('source3', None) 
            statecode = covdata.get('statecode', None)
            status_change_date = covdata.get('statuschangedate', None) 
            type_of_transmission = covdata.get('typeoftransmission', None)
            
            covid_data, created = Covid.objects.get_or_create(
                patient_number = patient_number,
                age = age,                     
                backup_notes = backup_notes,
                current_status = current_status,
                date_announced = date_announced,
                city = city,
                district = district,
                state = state,
                gender = gender,
                nationality = nationality,
                notes = notes,
                source1 = source1,
                source2 = source2,
                source3 = source3,
                statecode = statecode,
                status_change_date = status_change_date,
                type_of_transmission = type_of_transmission
            )
            if created:
                covid_data.save()

    def handle(self, *args, **options):
        """
        Makes a GET request to the API.
        """
        headers = {'Content-Type': 'application/json'}
        response = requests.get(
            url=IMPORT_URL,
            headers=headers,
        )
        covdata = response.json()
        covdata = covdata['raw_data']
        for k in range(len(covdata)):
            if covdata[k]['dateannounced']!='':
                covdata[k]['dateannounced'] = datetime.datetime.strptime(covdata[k]['dateannounced'], "%d/%m/%Y").strftime("%Y%m%d")
        df = pd.DataFrame(covdata)
        df_1=df.to_dict('list')
        #try:
        for j, data_object in df.iterrows():
            if df_1['dateannounced'][j]!='':
                self.import_covid_data(covdata[j])
            print("data stored")
        '''except Exception as e:
            print("something wrong")'''