from django.test import TestCase


# Create your tests here.

import requests


data = {
    'var1': 'this',
    'var2': 'that'
}

r = requests.post("http://api.example.com/v1/api/some/",
    files={'document': open('report.txt', 'rb')},
    data=data,
    headers={"Authorization": "Token jfhgfgsdadhfghfgvgjhN"} #since I had to authenticate for the same
)

print (r.json())