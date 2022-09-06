
import requests

city = input('Enter city name: ')
print(' Displaying Weather report: ', city)

url = 'https://wttr.in/{}'.format(city)
res = requests.get(url)

print(res.text)