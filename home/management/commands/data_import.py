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
    def import_covid_data(self, covdata, df, df_1):
        a=Covid.objects.values_list('patient_number', flat=True)
        try:     
            for j, data_object in df.iterrows():
                if df['patientnumber'][j]<=str(a[j]):
                    if df_1['dateannounced'][j]!='' and df_1['patientnumber'][j]!='':
                        age = covdata[j].get('agebracket')
                        backup_notes = covdata[j].get('backupnotes') 
                        current_status = covdata[j].get('currentstatus')
                        date_announced = covdata[j].get('dateannounced')
                        city = covdata[j].get('detectedcity') 
                        district = covdata[j].get('detecteddistrict')
                        state = covdata[j].get('detectedstate')
                        gender = covdata[j].get('gender')
                        nationality = covdata[j].get('nationality') 
                        notes = covdata[j].get('notes')
                        patient_number = covdata[j].get('patientnumber') 
                        source1 = covdata[j].get('source1')
                        source2 = covdata[j].get('source2') 
                        source3 = covdata[j].get('source3') 
                        statecode = covdata[j].get('statecode')
                        status_change_date = covdata[j].get('statuschangedate') 
                        type_of_transmission = covdata[j].get('typeoftransmission')
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
        except Exception as e:
            m=j
            for m, data_object in df.iterrows():
                if (m<j):
                    continue
                else:
                    if df_1['dateannounced'][m]!='' and df_1['patientnumber'][m]!='':
                        age = covdata[m].get('agebracket')
                        backup_notes = covdata[m].get('backupnotes') 
                        current_status = covdata[m].get('currentstatus')
                        date_announced = covdata[m].get('dateannounced')
                        city = covdata[m].get('detectedcity') 
                        district = covdata[m].get('detecteddistrict')
                        state = covdata[m].get('detectedstate')
                        gender = covdata[m].get('gender')
                        nationality = covdata[m].get('nationality') 
                        notes = covdata[m].get('notes')
                        patient_number = covdata[m].get('patientnumber') 
                        source1 = covdata[m].get('source1')
                        source2 = covdata[m].get('source2') 
                        source3 = covdata[m].get('source3') 
                        statecode = covdata[m].get('statecode')
                        status_change_date = covdata[m].get('statuschangedate') 
                        type_of_transmission = covdata[m].get('typeoftransmission')
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
            return m

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
        i = self.import_covid_data(covdata, df, df_1)
        #try:
        print("data stored")
        print(i)
        '''except Exception as e:
            print("something wrong")'''