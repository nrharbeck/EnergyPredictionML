import pandas as pd
#from pandas import json_normalize
import json
import urllib.request
import numpy as np
#API key from EIA.gov 
API_Key = #Insert Key Here

State_List = ['AL','AK','AZ','AR','CA','CO','CT','DE','FL','GA','HI','ID','IL','IN','IA','KS','KY','LA','ME','MD','MA','MI','MN','MS','MO','MT','NE','NV','NH','NJ','NM','NY','NC','ND','OH','OK','OR','PA','RI','SC','SD','TN','TX','UT','VT','VA','WA','WV','WI','WY']


df_raw=pd.DataFrame(np.empty((0,2)))
print("Start loading data...")

#Import Electric power carbon dioxide emissions and all fuels net generation
API_Calls = []
for i in State_List:
    CO2Emissions_API_Link = "http://api.eia.gov/series/?api_key="+str(API_Key)+"&series_id=EMISS.CO2-TOTV-EC-TO-"+str(i)+".A"
    Coal_API_Link = "http://api.eia.gov/series/?api_key="+str(API_Key)+"&series_id=ELEC.GEN.COW-"+str(i)+'-99.A'
    PetLi_API_Link = "http://api.eia.gov/series/?api_key="+str(API_Key)+"&series_id=ELEC.GEN.PEL-"+str(i)+'-99.A'
    PetCoke_API_Link = "http://api.eia.gov/series/?api_key="+str(API_Key)+"&series_id=ELEC.GEN.PC-"+str(i)+'-99.A'
    NatGas_API_Link = "http://api.eia.gov/series/?api_key="+str(API_Key)+"&series_id=ELEC.GEN.NG-"+str(i)+'-99.A'
    OtGas_API_Link = "http://api.eia.gov/series/?api_key="+str(API_Key)+"&series_id=ELEC.GEN.OOG-"+str(i)+'-99.A'
    Nuclear_API_Link = "http://api.eia.gov/series/?api_key="+str(API_Key)+"&series_id=ELEC.GEN.NUC-"+str(i)+'-99.A'
    Hydro_API_Link = "http://api.eia.gov/series/?api_key="+str(API_Key)+"&series_id=ELEC.GEN.HYC-"+str(i)+'-99.A'
    OtRenew_API_Link = "http://api.eia.gov/series/?api_key="+str(API_Key)+"&series_id=ELEC.GEN.AOR-"+str(i)+'-99.A'
    Wind_API_Link = "http://api.eia.gov/series/?api_key="+str(API_Key)+"&series_id=ELEC.GEN.WND-"+str(i)+'-99.A'
    Solar_API_Link = "http://api.eia.gov/series/?api_key="+str(API_Key)+"&series_id=ELEC.GEN.SUN-"+str(i)+'-99.A'
    PV_API_Link = "http://api.eia.gov/series/?api_key="+str(API_Key)+"&series_id=ELEC.GEN.SPV-"+str(i)+'-99.A'
    Thermal_API_Link = "http://api.eia.gov/series/?api_key="+str(API_Key)+"&series_id=ELEC.GEN.STH-"+str(i)+'-99.A'
    Geothermal_API_Link = "http://api.eia.gov/series/?api_key="+str(API_Key)+"&series_id=ELEC.GEN.GEO-"+str(i)+'-99.A'
    Wood_API_Link = "http://api.eia.gov/series/?api_key="+str(API_Key)+"&series_id=ELEC.GEN.WWW-"+str(i)+'-99.A'
    Biomass_API_Link = "http://api.eia.gov/series/?api_key="+str(API_Key)+"&series_id=ELEC.GEN.WAS-"+str(i)+'-99.A'
    HydroElectric_API_Link = "http://api.eia.gov/series/?api_key="+str(API_Key)+"&series_id=ELEC.GEN.HPS-"+str(i)+'-99.A'
    Other_API_Link = "http://api.eia.gov/series/?api_key="+str(API_Key)+"&series_id=ELEC.GEN.OTH-"+str(i)+'-99.A'
    AllSolar_API_Link = "http://api.eia.gov/series/?api_key="+str(API_Key)+"&series_id=ELEC.GEN.TSN-"+str(i)+'-99.A'
    SmallPV_API_Link = "http://api.eia.gov/series/?api_key="+str(API_Key)+"&series_id=ELEC.GEN.DPV-"+str(i)+'-99.A'
    Link = [CO2Emissions_API_Link, Coal_API_Link, PetLi_API_Link, PetCoke_API_Link, NatGas_API_Link, OtGas_API_Link, Nuclear_API_Link, Hydro_API_Link, OtRenew_API_Link, Wind_API_Link, Solar_API_Link, PV_API_Link, Thermal_API_Link, Geothermal_API_Link, Wood_API_Link, Biomass_API_Link, HydroElectric_API_Link, Other_API_Link, AllSolar_API_Link, SmallPV_API_Link]
    API_Calls.extend(Link)

#Create dataframe from JSON file where series are available
for j in API_Calls:
    try:
        with urllib.request.urlopen(j) as url:
            data = json.loads(url.read().decode())
        df_iteration = pd.json_normalize(data["series"], 'data', ['series_id', 'name','units','f','description','copyright','source','iso3166','geography','start','end'])
        df_raw = df_raw.append(df_iteration)
    except:
        KeyError

df = df_raw

#Save to csv for additional formatting
df.to_csv("Data/EIA_A_Raw_Data.csv")


