import requests
from bs4 import BeautifulSoup

url = 'https://www.weather.com/en-US/weather/today/l/USNY0996:1:US'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
temp = soup.find('span', {'data-testid': 'TemperatureValue'}).text




print('The local tempeture today is ', temp ,' Currently.')
