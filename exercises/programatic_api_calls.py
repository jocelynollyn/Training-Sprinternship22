import requests

url = 'https://api.coindesk.com/v1/bpi/currentprice.json'

# make get request
response = requests.get(url)


# check if response status code is 200
if response.status_code == 200:
    # get response body in text
    print(response.text)

    # convert response body to JSON
    data = response.json()


# otherwise, print error code
else:
    print(response.status_code)