import pandas as pd
import pickle
from collections import defaultdict

# Step 1: Read Excel File and Create a Dictionary
excel_data = pd.read_excel('your_excel_file.xlsx', usecols=['country', 'city'])

# Clean the data: remove cities with asterisks
excel_data['city'] = excel_data['city'].replace(r'\*','', regex=True).str.strip()

# Create a defaultdict
excel_dict = defaultdict(list)
for index, row in excel_data.iterrows():
    excel_dict[row['country']].append(row['city'])

# Step 2: Load the .pkl file
with open('your_file.pkl', 'rb') as file:
    country_cities = pickle.load(file)

# Step 3: Enrich the .pkl file
for country, cities in excel_dict.items():
    if country in country_cities:
        country_cities[country] = list(set(country_cities[country] + cities))
    else:
        country_cities[country] = cities

# Step 4: Save the updated data
with open('enriched_file.pkl', 'wb') as file:
    pickle.dump(country_cities, file)