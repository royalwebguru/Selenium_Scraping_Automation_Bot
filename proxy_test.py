import requests

# Define the proxy details
proxy = {
    'http': 'http://Dean50GB:Dean50GB123_country-fr_session-2ut6f29p_lifetime-24h@geo.iproyal.com:12321',
    'https': 'http://Dean50GB:Dean50GB123_country-fr_session-2ut6f29p_lifetime-24h@geo.iproyal.com:12321'
}

# Make a request using the proxy
response = requests.get('https://www.metin2pserver.info/vote.htm?id=kime2com&name=196')

# Print the response
print(response.text)