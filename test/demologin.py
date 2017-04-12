import requests
requests.adapters.DEFAULT_RETRIES = 5

#r = requests.get('http://localhost:9004?type=login&account=hao&passwd=123')
r = requests.get('http://localhost:9004?type=pubkey')
print(r.text)


