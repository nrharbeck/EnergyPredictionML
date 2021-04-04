import pandas as pd 

State_List = ['AL','AK','AZ','AR','CA','CO','CT','DE','FL','GA','HI','ID','IL','IN','IA','KS','KY','LA','ME','MD','MA','MI','MN','MS','MO','MT','NE','NV','NH','NJ','NM','NY','NC','ND','OH','OK','OR','PA','RI','SC','SD','TN','TX','UT','VT','VA','WA','WV','WI','WY']

 
df_raw = pd.read_csv("Data/program.csv")
df = df_raw
df = df.rename(columns={'id': 'program_id'})

df_stateID = pd.read_csv("Data/state.csv")
df_implementingSector = pd.read_csv("Data/implementing_sector.csv")
df_programCategory = pd.read_csv("Data/program_category.csv")
df_programType = pd.read_csv("Data/program_type.csv")
df_technology = pd.read_csv("Data/technology.csv")
df_technologyCategory = pd.read_csv("Data/technology_category.csv")
df_programTechnology = pd.read_csv("Data/program_technology.csv")
df_parameterSet = pd.read_csv("Data/parameter_set.csv")
df_parameterSet = df_parameterSet.rename(columns={'id': 'parameter_set_id'})
df_parameter = pd.read_csv("Data/parameter.csv")

df_programTechnology['technology_category'] = df_technology['technology_category_id']
df = df.merge(df_programTechnology, how= 'left', on = "program_id")
df = df.merge(df_parameterSet, how= 'left', on = "program_id")


df['technology_category'] = df['technology_id']
df = df.merge(df_parameter, how= 'left', on = "parameter_set_id")

df['state_id'] = df['state_id'].map(df_stateID.set_index('id')['name'])
df['implementing_sector_id'] = df['implementing_sector_id'].map(df_implementingSector.set_index('id')['name'])
df['program_category_id'] = df['program_category_id'].map(df_programCategory.set_index('id')['name'])
df['program_type_id'] = df['program_type_id'].map(df_programType.set_index('id')['name'])
df['technology_id'] = df['technology_id'].map(df_technology.set_index('id')['name'])
df['technology_category'] = df['technology_category'].map(df_technology.set_index('id')['technology_category_id'])
df['technology_category'] = df['technology_category'].map(df_technologyCategory.set_index('id')['name'])




df_dsire = df.drop(columns=['created_by_user_id','fromSir'])

#Filter out non U.S. states
df_states = df_dsire[(df_dsire["state_id"] != "American Samoa") & (df_dsire["state_id"] != "District of Columbia") & (df_dsire["state_id"] != "Federated States of Micronesia") & (df_dsire["state_id"] != "Guam") & (df_dsire["state_id"] != "Federal") & (df_dsire["state_id"] != "N. Mariana Islands") & (df_dsire["state_id"] != "Palau") & (df_dsire["state_id"] != "Puerto Rico") & (df_dsire["state_id"] != "Virgin Islands")]

print(df_states.columns)

#df_states.to_csv("Data/DSIRE_Formatted.csv")
