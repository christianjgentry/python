import requests

test = requests.get('http://pokeapi.co/api/v2/berry/16')

ye = test.json()

print(ye.headers)
