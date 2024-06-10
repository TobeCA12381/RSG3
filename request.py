import requests

r = requests.get('http://localhost:8093/')
print (r.json())
