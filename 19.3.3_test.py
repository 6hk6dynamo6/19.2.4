import requests
import json

#get
status = 'available'
res = requests.get(f"https://petstore.swagger.io/v2/pet/findByStatus?status={status}", headers = {'accept': 'application/json'})
print(res.status_code)
print(res.text)
print(res.json())
print(type(res.json()))

res = requests.get(f"https://petstore.swagger.io/v2/pet/94944949494949490", headers = {'accept': 'application/json'})
print(res.status_code)
print(res.text)
print(res.json())
print(type(res.json()))


# #post
data = {
  "id": 94944949494949490,
  "category": {
    "id": 0,
    "name": "string"
  },
  "name": "petra",
  "photoUrls": [
    "string"
  ],
  "tags": [
    {
      "id": 0,
      "name": "string"
    }
  ],
  "status": "available"
}
data = json.dumps(data)
res = requests.post(f"https://petstore.swagger.io/v2/pet/", headers = {'accept': 'application/json','Content-Type': 'application/json'}, data = data)
print(res.status_code)
print(res.json())

#put

data = {
  "id": 94944949494949490,
  "category": {
    "id": 0,
    "name": "string"
  },
  "name": "petr",
  "photoUrls": [
    "string"
  ],
  "tags": [
    {
      "id": 0,
      "name": "string"
    }
  ],
  "status": "available"
}
data = json.dumps(data)
headers = {'accept': 'application/json','Content-Type': 'application/json'}
url = f"https://petstore.swagger.io/v2/pet/"
res = requests.put(url = url, headers = headers , data = data)
print(res.status_code)
print(res.json())

#DELETE

petid = '94944949494949490'
url = f'https://petstore.swagger.io/v2/pet/{petid}'
headers = {'accept': 'application/json'}
res = requests.delete(url, headers = headers)
print(res.status_code)
print(res.json())