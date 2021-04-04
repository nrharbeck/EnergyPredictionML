import pandas as pd
from pandas import json_normalize
import json
import urllib.request
import numpy as np 
import datetime
d = datetime.datetime.today()

states = {
        'USA-AK': 'Alaska',
        'USA-AL': 'Alabama',
        'USA-AR': 'Arkansas',
        'USA-AS': 'American Samoa',
        'USA-AZ': 'Arizona',
        'USA-CA': 'California',
        'USA-CO': 'Colorado',
        'USA-CT': 'Connecticut',
        'USA-DC': 'District of Columbia',
        'USA-DE': 'Delaware',
        'USA-FL': 'Florida',
        'USA-GA': 'Georgia',
        'USA-GU': 'Guam',
        'USA-HI': 'Hawaii',
        'USA-IA': 'Iowa',
        'USA-ID': 'Idaho',
        'USA-IL': 'Illinois',
        'USA-IN': 'Indiana',
        'USA-KS': 'Kansas',
        'USA-KY': 'Kentucky',
        'USA-LA': 'Louisiana',
        'USA-MA': 'Massachusetts',
        'USA-MD': 'Maryland',
        'USA-ME': 'Maine',
        'USA-MI': 'Michigan',
        'USA-MN': 'Minnesota',
        'USA-MO': 'Missouri',
        'USA-MP': 'Northern Mariana Islands',
        'USA-MS': 'Mississippi',
        'USA-MT': 'Montana',
        'USA-NA': 'National',
        'USA-NC': 'North Carolina',
        'USA-ND': 'North Dakota',
        'USA-NE': 'Nebraska',
        'USA-NH': 'New Hampshire',
        'USA-NJ': 'New Jersey',
        'USA-NM': 'New Mexico',
        'USA-NV': 'Nevada',
        'USA-NY': 'New York',
        'USA-OH': 'Ohio',
        'USA-OK': 'Oklahoma',
        'USA-OR': 'Oregon',
        'USA-PA': 'Pennsylvania',
        'USA-PR': 'Puerto Rico',
        'USA-RI': 'Rhode Island',
        'USA-SC': 'South Carolina',
        'USA-SD': 'South Dakota',
        'USA-TN': 'Tennessee',
        'USA-TX': 'Texas',
        'USA-UT': 'Utah',
        'USA-VA': 'Virginia',
        'USA-VI': 'Virgin Islands',
        'USA-VT': 'Vermont',
        'USA-WA': 'Washington',
        'USA-WI': 'Wisconsin',
        'USA-WV': 'West Virginia',
        'USA-WY': 'Wyoming'
}

#This code formats the dataframe for the API calls
df_DSIRE = pd.read_csv("Data/DSIRE_Formatted.csv")
df_DSIRE = df_DSIRE.set_index('program_id')

df_DSIRE['start_date'] = pd.to_datetime(df_DSIRE['start_date'])
df_DSIRE['end_date'] = pd.to_datetime(df_DSIRE['end_date'])
df_DSIRE['created_ts'] = pd.to_datetime(df_DSIRE['created_ts'])
df_DSIRE['updated_ts'] = pd.to_datetime(df_DSIRE['updated_ts'])


def update_date(row):
    if row['start_date'] is pd.NaT:
        if row['created_ts'] is pd.NaT:
            return row['updated_ts']
        else: 
            return row['created_ts']
    else:
        return row['start_date']

df_DSIRE['recent_date'] = df_DSIRE.apply(lambda row: update_date(row), axis=1)

#print(df_DSIRE[['recent_date', 'start_date', 'updated_ts', 'created_ts']])

df_EIA_A = pd.read_csv("Data/EIA_A_Raw_Data.csv")

df_EIA_A.set_axis(['Index','Date','Generation','Copyright','description','end','f','geography','iso3166','name','series_id','source','start','units'], axis=1, inplace=True)
df_EIA_A['Date'] = pd.to_datetime(df_EIA_A['Date'], format = "%Y")
df_EIA_A['State'] = df_EIA_A['geography'].map(states)

print('Data Loaded. Transforming (this will take some time)...')

"""
#Use this combination for higher leve overview
col_names = ['Solar', 'Wind', 'Biomass', 'Geothermal', 'Hydro']
policy_types = ['Financial Incentive', 'Regulatory Policy']
for i in col_names:
    df_policy = df_DSIRE[df_DSIRE['technology_category'].str.contains(i)==True]
    for j in policy_types:
        df_types = df_policy[df_policy['program_category_id'].str.contains(j)==True]
        df_EIA_A[i+str('_')+j] = df_EIA_A.apply(lambda row: df_types[((row['Date']>df_types['recent_date']) & (df_types['state_id'].str.contains(row['State'])))].shape[0], axis=1)
    print(i,'Done')
"""
df_technologies = pd.read_csv('Data/technology.csv')
col_names = df_technologies['name'].unique()
policy_types = ['Financial Incentive', 'Regulatory Policy']
for i in col_names:
    df_policy = df_DSIRE[df_DSIRE['technology_id'].str.contains(i)==True]
    for j in policy_types:
        df_types = df_policy[df_policy['program_category_id'].str.contains(j)==True]
        df_EIA_A[i+str('_')+j] = df_EIA_A.apply(lambda row: df_types[((row['Date']>df_types['recent_date']) & (df_types['state_id'].str.contains(row['State'])))].shape[0], axis=1)
    print(i,'Done')

print(df_EIA_A)
df_EIA_A.to_csv("Data/EIA_DSIRE_Data_Tech.csv")
