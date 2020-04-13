import  os
import requests
import pandas as pd

def get_covid():
    url = 'https://api.covid19india.org/raw_data.json'
    response = requests.get(url)
    covdata = response.json()
    covdata = covdata['raw_data']
    df = pd.DataFrame(covdata)
    covdata_list = []
    for i, rows in df.iterrows():
        my_list = [rows.agebracket,
                rows.backupnotes,
                rows.currentstatus,
                rows.dateannounced,
                rows.detectedcity,
                rows.detecteddistrict,
                rows.detectedstate,
                rows.gender,
                rows.nationality,
                rows.notes,
                rows.patientnumber,
                rows.source1,
                rows.source2,
                rows.source3,
                rows.statecode,
                rows.statuschangedate,
                rows.typeoftransmission
        ]
        covdata_list.append(covdata[i])
    return covdata_list