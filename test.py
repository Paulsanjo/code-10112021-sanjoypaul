
import requests

# header type is application/json
headers = {'Content-Type': 'application/json', 'Accept':'application/json'}

data = [{"Gender": "Male", "HeightCm": 171, "WeightKg": 96 },
{ "Gender": "Male", "HeightCm": 161, "WeightKg": 85 },
{ "Gender": "Male", "HeightCm": 180, "WeightKg": 77 },
{ "Gender": "Female", "HeightCm": 166, "WeightKg": 62},
{"Gender": "Female", "HeightCm": 150, "WeightKg": 70},
{"Gender": "Female", "HeightCm": 167, "WeightKg": 82},
{"Gender": "Male", "HeightCm": 170, "WeightKg": 83},
{"Gender": "Female", "HeightCm": 156, "WeightKg": 94},
{"Gender": "Male", "HeightCm": 160, "WeightKg": 99}]
# Making a POST request
r = requests.post('http://127.0.0.1:8000/', json=data,  headers=headers)
 
# check status code for response received
# success code - 200
print(r)
 
# print content of request
print(r.json())