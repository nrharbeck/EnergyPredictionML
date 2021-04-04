import pandas as pd

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

df_A = pd.read_csv("Data/EIA_A_Raw_Data.csv")
df_M = pd.read_csv("Data/EIA_M_Raw_Data.csv")

df_A.set_axis(['Index','Date','Generation','Copyright','description','end','f','geography','iso3166','name','series_id','source','start','units'], axis=1, inplace=True)
df_A['Date'] = pd.to_datetime(df_A['Date'], format = "%Y")
df_A['State'] = df_A['geography'].map(states)

df_M.set_axis(['Index','Date','Generation','Copyright','description','end','f','geography','iso3166','name','series_id','source','start','units'], axis=1, inplace=True)
df_M['Date'] = pd.to_datetime(df_M['Date'], format = "%Y%m")
df_M['State'] = df_M['geography'].map(states)


df_M = df_M.groupby([df_M.series_id, df_M.State, df_M.start, df_M.description, df_M.end, df_M.Date.dt.year,])['Generation'].sum()
df_A = df_A.groupby([df_A.series_id, df_A.State, df_A.start, df_A.description, df_A.end, df_A.Date.dt.year,])['Generation'].sum()

print(df_A)
print(df_M) 