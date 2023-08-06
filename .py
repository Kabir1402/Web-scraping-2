import requests
from bs4 import BeautifulSoup
import pandas as pd

# Define the URL
START_URL = "https://en.wikipedia.org/wiki/List_of_brown_dwarfs"

# Make a page request using the requests module
response = requests.get(START_URL)

# Get all the tables of the page using find_all() method
soup = BeautifulSoup(response.text, 'html.parser')
tables = soup.find_all('table', {'class': 'wikitable'})

# Create empty lists to store star data
star_data = []

# Loop through each table
for table in tables:
    rows = table.find_all('tr')
    
    # Loop through each row (skipping the header row)
    for row in rows[1:]:
        data = row.find_all('td')
        star_info = [d.text.strip() for d in data]
        star_data.append(star_info)

# Create empty lists to store star attributes
star_names = []
star_radius = []
star_mass = []
star_distance = []

# Loop through the star data list to extract specific attributes
for star_info in star_data:
    if len(star_info) >= 4:
        star_names.append(star_info[0])
        star_radius.append(star_info[1])
        star_mass.append(star_info[2])
        star_distance.append(star_info[3])

# Create a DataFrame using pandas
data = {
    'Star Name': star_names,
    'Radius': star_radius,
    'Mass': star_mass,
    'Distance': star_distance
}

df = pd.DataFrame(data)

# Create a CSV file from the DataFrame
df.to_csv('brown_dwarfs.csv', index=False)

print("Data scraped and saved to 'brown_dwarfs.csv'")
