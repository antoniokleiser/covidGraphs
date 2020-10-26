import requests
import json
import pandas as pd
import matplotlib.pyplot as plt

# url = 'https://api.covid19api.com/summary'
# url = 'https://api.covid19api.com/countries'
#url = "https://api.covid19api.com/dayone/country/spain/status/confirmed"

url = 'https://api.covid19api.com/country/spain/status/confirmed?from=2020-02-01T00:00:00Z&to=2020-10-17T00:00:00Z'

response = requests.get(url)
print(response)

# USAR CON SUMMARY
# payload = {}
# headers = {}
#
# response = requests.request("GET", url, headers=headers, data = payload)
#
# print(response.text.encode('utf8'))

# USAR CON COUNTRIES
# payload = {}
# headers = {}
#
# response = requests.request("GET", url, headers=headers, data=payload)
#
# print(response.text.encode('utf8'))

# USAR CON COUNTRY AND STATUS
#payload = {}
#headers = {}
#
#response = requests.request("GET", url, headers=headers, data=payload)
#
#print(response.text.encode('utf8'))

# PRUEBA TOTAL

payload = {}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)


# print(response.text.encode('utf8'))
df = pd.json_normalize(response.json())
#df = pd.DataFrame(response)

df.to_excel('../data/datos.xlsx')
dat = pd.read_excel('../data/datos.xlsx')

plt.plot(df['Date'], df['Cases'])
plt.show()
