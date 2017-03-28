import folium
from folium.plugins import MarkerCluster
import pandas as pd

geomap = pd.read_csv('10305311data.csv',encoding='latin-1')

map10305 = folium.Map(location=[40.74,-74.125])

coords = []
popups = []
icons = []

for index, row in geomap.iterrows():
    complaint = row["Complaint Type"]
    lat=row['Latitude']
    lon=row['Longitude']
    coords.append([lat,lon])
    popups.append(complaint)
    icons.append(folium.Icon(color='red'))

map10305.add_children(MarkerCluster(locations=coords,popups=popups,icons=icons))
        
map10305.save(outfile='311dataRosebank.html')

