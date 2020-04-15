import  os
import requests
import pandas as pd

def dashboard_covid():
    url = '	https://api.covid19india.org/data.json'
    response = requests.get(url)
    trackdata = response.json()
    trackstatewise = trackdata['statewise'][1:]
    df = pd.DataFrame(trackstatewise)
    trackdata_list = []
    for i, rows in df.iterrows():
        my_list = [rows.state,
                rows.confirmed,
                rows.active,
                rows.recovered,
                rows.deaths,
                rows.deltaconfirmed,
                rows.deltadeaths,
                rows.deltarecovered
        ]
        trackdata_list.append(trackstatewise[i])
    return trackdata_list