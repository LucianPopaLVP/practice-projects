import requests

url = 'https://api.pwnedpasswords.com/range/'+ 'password'
res = requests.get(url)
print(res)

