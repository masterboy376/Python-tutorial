import requests
#  get 
r=requests.get('https://financialmodelingprep.com/api/company/price/AAPL')
print(r)
print(r.status_code)

# post 
data={
    'content-type':"application/json"
}
url="ghjj.com"
r1= requests.post(url=url, data=data)
print(r1)
print(r1.status_code)