import requests

url = "http://127.0.0.1:9696/predict"
# customer = {"contract": "two_year", "tenure": 1, "monthlycharges": 10}
customer = {"contract": "two_year", "tenure": 12, "monthlycharges": 10}
result = requests.post(url, json=customer).json()

print(result)