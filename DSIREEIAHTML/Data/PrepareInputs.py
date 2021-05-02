import pandas as pd
import numpy as np


df = pd.read_csv("https://raw.githubusercontent.com/nrharbeck/EnergyPredictionML/main/DataProcessing/EIA_DSIRE_Data_Tech.csv")

#Drop any NA rows for model building
df = df.dropna(how='any')

#Remove CO2 emissions
df = df[~df.series_id.str.contains("EMISS.CO2-TOTV")]

#Make a new column with the EIA generation categories
df['generation_energy'] = df['series_id'].str[9:-8]
all_dates = df['Date'].unique()


#Select only most recent data for real time predictions
df2 = df.groupby(['generation_energy','State'],as_index=False).agg({'Date':'max'})

for date in range(len(all_dates)):
    df2 = df2.append(pd.Series(0, index=df2.columns), ignore_index=True)
    df2['Date'].iloc[-1] = all_dates[date]

for date in range(len(all_dates)):
    df = df.append(pd.Series(0, index=df.columns), ignore_index=True)
    df['Date'].iloc[-1] = all_dates[date]

df = df.merge(df2, on=['Date','generation_energy', 'State'])

#Guide to see if strings changse from https://stackoverflow.com/questions/40348541/pandas-diff-with-string
df['Series_Change'] = df['series_id'].ne(df['series_id'].shift().bfill()).astype(int)
df["Generation_Diff"] = np.where(-df['Generation'].diff() > 0, 1, 0) 
df['Generation_Increase'] = np.where((df["Generation_Diff"] > 0) & (df['Series_Change'] == 0), 1, 0)

#Split data into features and target. Descriptive EIA data is removed here.
X = df.drop(columns=['Generation', 'Series_Change', 'Generation_Diff', 'Generation_Increase', 'Unnamed: 0', 'Index', 'units', 'Copyright', 'description','end','f','geography','iso3166','name','source','start', 'series_id'])
y = df['Generation_Increase']

#Encode categorical features
#print(X.columns)
X = pd.get_dummies(X, columns=['Date','generation_energy','State'])
#Remove rows with all zeros from columns
X = X.drop(columns='generation_energy_0')
X = X.drop(columns='State_0')


#Export for reading into HTML/JS
X.to_csv("DSIREEIAHTML/Data/modelinput.csv", index=False)