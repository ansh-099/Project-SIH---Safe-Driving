import requests
url = 'http://localhost:5000/api'
r = requests.post(url,json={'exp':[0.21531516644139326,0.15005541484228635,0.7914562008951398,-2.,39.,-62.,76.,55.,65.],})
print(r.text)
