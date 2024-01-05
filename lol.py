# Load the original .pkl file
with open('your_file.pkl', 'rb') as file:
    original_data = pickle.load(file)

# Load the new .pkl file
with open('your_new_file_name.pkl', 'rb') as file:
    new_data = pickle.load(file)

# Count the number of countries and cities in the original data
original_countries_count = len(original_data)
original_cities_count = sum(len(cities) for cities in original_data.values())

# Count the number of countries and cities in the new data
new_countries_count = len(new_data)
new_cities_count = sum(len(cities) for cities in new_data.values())

# Calculate the percentage increase
country_increase_percent = ((new_countries_count - original_countries_count) / original_countries_count) * 100 if original_countries_count > 0 else 100
city_increase_percent = ((new_cities_count - original_cities_count) / original_cities_count) * 100 if original_cities_count > 0 else 100

print(f"Percentage increase in countries: {country_increase_percent:.2f}%")
print(f"Percentage increase in cities: {city_increase_percent:.2f}%")
