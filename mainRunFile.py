'''First attempt, not sure what it does'''
import requests

# Set our variables for the request we want to make
#base_url = 'https://disneyworld.disney.go.com/availability-calendar/api/calendar'
#start_date = '2022-05-15'
#end_date = '2022-05-21'

base_url = 'https://disneyworld.disney.go.com/finder/api/v1/explorer-service/dining-availability/%7BD7B825B5-061E-4CD1-8DCC-1950A408F3DC%7D/wdw/19634138;entityType=restaurant/table-service/1/2023-06-16/?searchTime=18:00:00'

# Add a header so that the request looks legit
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:98.0) Gecko/20100101 Firefox/98.0',
}

# Set our URL parameters to get the data we want
params = {
    'segment': 'tickets',
    'startDate': start_date,
    'endDate': end_date,
}

# Using the above data, make our request, and get our response
response = requests.get(
    base_url,
    headers=headers,
    params=params,
    timeout=0.001,
)

# Convert the data from a JSON string to a python dictionary
data = response.json()
