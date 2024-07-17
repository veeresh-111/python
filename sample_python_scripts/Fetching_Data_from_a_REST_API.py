import requests

response = requests.get('https://api.github.com/repos/python/cpython')
data = response.json()

print("Repository:", data['name'])
print("Description:", data['description'])
print("Stars:", data['stargazers_count'])
