import requests
requests.adapters.DEFAULT_RETRIES = 5

r = requests.get('http://localhost:9003?type=login&account=hao&passwd=13')
print(r.text)


