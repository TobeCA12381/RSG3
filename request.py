import requests

r = requests.get('http://http://localhost:8093/')
print (r.json())